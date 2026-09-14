"""Surgical repair: reload only the removals table (with the departed_date ->
departure_date table-scoped rename fix), re-dedup it, and regenerate the
derived objects (views, _metadata, _columns, DICTIONARY.md) in the existing
ice.duckdb. Avoids a full 53-minute rebuild for a one-table fix."""
from pathlib import Path

import duckdb

from build_database import (
    DEDUP_KEYS,
    build_columns_table,
    build_metadata,
    create_views,
    dedup_table,
    discover_sources,
    export_dictionary,
    load_table,
    run_validation,
)

db_path = Path("ice.duckdb")
con = duckdb.connect(str(db_path))
con.execute("SET preserve_insertion_order = false")
con.execute(f"SET temp_directory = '{db_path.resolve()}.tmp'")

sources = discover_sources(Path("data/raw"))
chunks = sources["removals"]
print(f"Reloading removals from {len(chunks)} sheets")

con.execute("DROP TABLE IF EXISTS removals")
rc = load_table(con, "removals", chunks)
print(f"loaded: {rc:,}")

removed = dedup_table(con, "removals", DEDUP_KEYS["removals"])
print(f"dedup removed: {removed:,}")
con.execute("CHECKPOINT")

null_2026 = con.execute(
    "SELECT COUNT(*) FROM removals WHERE data_source='release_2026' AND departure_date IS NULL"
).fetchone()[0]
rng = con.execute(
    "SELECT data_source, COUNT(*), MIN(departure_date), MAX(departure_date) FROM removals GROUP BY 1 ORDER BY 1"
).fetchall()
print(f"release_2026 rows with NULL departure_date: {null_2026:,}")
for r in rng:
    print(" ", r)

built = {"arrests", "detainers", "detentions", "encounters", "rca_decisions", "removals"}
print("Recreating views")
create_views(con, built)
print("Rebuilding metadata")
build_metadata(con, built)
run_validation(con, db_path)
print("Rebuilding _columns")
build_columns_table(con)
print("Exporting DICTIONARY.md")
export_dictionary(con, db_path.parent / "DICTIONARY.md")
con.execute("CHECKPOINT")
con.close()
print("REPAIR DONE")
