"""Apply the July 2026 audit fixes to the built ice.duckdb without a rebuild.

1. Delete release_2023 detention segments whose STAY was active on/after
   2022-10-01 (the original supersede keyed on segment book-out and left
   orphaned pre-boundary segments of boundary-spanning stays).
2. Delete exact whole-row duplicate encounters rows (non-null unique_id only;
   fully-redacted rows are left alone since identical redacted rows may be
   distinct real events).
3. Recreate views (now stay-level and date-constrained) and derived objects.
"""
from pathlib import Path

import duckdb

from build_database import (
    build_columns_table,
    build_metadata,
    create_views,
    export_dictionary,
    run_validation,
)

db_path = Path("ice.duckdb")
con = duckdb.connect(str(db_path))
con.execute("SET preserve_insertion_order = false")
con.execute(f"SET temp_directory = '{db_path.resolve()}.tmp'")
con.execute("SET memory_limit = '8GB'")

print("[1/4] Deleting boundary-spanning release_2023 detention stays")
before = con.execute("SELECT COUNT(*) FROM detentions").fetchone()[0]
con.execute("""
    DELETE FROM detentions
    WHERE data_source = 'release_2023'
      AND (stay_book_out_date >= DATE '2022-10-01'
           OR stay_book_out_date IS NULL)
""")
after = con.execute("SELECT COUNT(*) FROM detentions").fetchone()[0]
print(f"  detentions: {before:,} -> {after:,} ({before - after:,} deleted)")

print("[2/4] Deduplicating exact whole-row duplicate encounters")
cols = [
    r[0] for r in con.execute(
        "SELECT column_name FROM information_schema.columns "
        "WHERE table_name = 'encounters' ORDER BY ordinal_position"
    ).fetchall()
]
col_list = ", ".join(f'"{c}"' for c in cols)
before = con.execute("SELECT COUNT(*) FROM encounters").fetchone()[0]
con.execute(f"""
    CREATE TEMP TABLE _enc_keep AS
    SELECT MIN(rowid) AS _rid
    FROM encounters
    WHERE unique_id IS NOT NULL
    GROUP BY {col_list}
""")
con.execute("""
    DELETE FROM encounters
    WHERE unique_id IS NOT NULL
      AND rowid NOT IN (SELECT _rid FROM _enc_keep)
""")
con.execute("DROP TABLE _enc_keep")
after = con.execute("SELECT COUNT(*) FROM encounters").fetchone()[0]
print(f"  encounters: {before:,} -> {after:,} ({before - after:,} deleted)")

built = {"arrests", "detainers", "detentions", "encounters", "rca_decisions", "removals"}

print("[3/4] Recreating views and derived objects")
create_views(con, built)
build_metadata(con, built)
run_validation(con, db_path)
build_columns_table(con)
export_dictionary(con, db_path.parent / "DICTIONARY.md")

print("[4/4] Sanity-checking the rewritten views")
n_arrests = con.execute("SELECT COUNT(*) FROM arrests").fetchone()[0]
n_view = con.execute("SELECT COUNT(*) FROM v_arrest_to_detention").fetchone()[0]
neg = con.execute(
    "SELECT COUNT(*) FROM v_arrest_to_detention WHERE days_arrest_to_detention < 0"
).fetchone()[0]
matched = con.execute(
    "SELECT COUNT(*) FROM v_arrest_to_detention WHERE stay_book_in_date IS NOT NULL"
).fetchone()[0]
print(f"  v_arrest_to_detention: {n_view:,} rows vs {n_arrests:,} arrests "
      f"(must be equal), {matched:,} matched, {neg:,} negative durations (must be 0)")
n_pipe = con.execute("SELECT COUNT(*) FROM v_enforcement_pipeline").fetchone()[0]
neg2 = con.execute(
    "SELECT COUNT(*) FROM v_enforcement_pipeline "
    "WHERE days_to_removal < 0 OR days_to_detention < 0"
).fetchone()[0]
print(f"  v_enforcement_pipeline: {n_pipe:,} rows, {neg2:,} negative durations (must be 0)")
n_stays = con.execute("SELECT COUNT(*) FROM v_detention_stays").fetchone()[0]
print(f"  v_detention_stays: {n_stays:,} stays from {after and con.execute('SELECT COUNT(*) FROM detentions').fetchone()[0]:,} segments")

assert n_view == n_arrests, "v_arrest_to_detention must be one row per arrest"
assert n_pipe == n_arrests, "v_enforcement_pipeline must be one row per arrest"
assert neg == 0 and neg2 == 0, "negative durations must be impossible by construction"

con.execute("CHECKPOINT")
con.close()
print("AUDIT REPAIR DONE")
