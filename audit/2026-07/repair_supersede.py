"""Apply the cross-release supersede to the already-built ice.duckdb and
regenerate derived objects, avoiding another full rebuild."""
from pathlib import Path

import duckdb

from build_database import (
    apply_supersede,
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

built = {"arrests", "detainers", "detentions", "encounters", "rca_decisions", "removals"}
print("Superseding overlapping release windows")
apply_supersede(con, built)
con.execute("CHECKPOINT")

print("\nFinal counts:")
for t in sorted(built):
    n = con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
    print(f"  {t}: {n:,}")

print("\nRecreating views")
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
print("SUPERSEDE REPAIR DONE")
