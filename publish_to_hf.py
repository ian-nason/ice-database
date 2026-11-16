#!/usr/bin/env python3
"""Upload ice.duckdb to Hugging Face for remote access.

Usage:
    uv run python publish_to_hf.py
    uv run python publish_to_hf.py --db ice.duckdb --repo Nason/ice-database
    HF_TOKEN=hf_xxx uv run python publish_to_hf.py
"""

import argparse
import sys
from pathlib import Path

import duckdb
from huggingface_hub import HfApi, create_repo


def generate_dataset_card(db_path: str) -> str:
    """Generate a HF-compatible README with YAML frontmatter."""
    con = duckdb.connect(db_path, read_only=True)
    metadata = con.sql(
        "SELECT table_name, description, row_count, column_count, "
        "data_sources, date_range FROM _metadata ORDER BY row_count DESC"
    ).fetchdf()
    con.close()

    table_rows = "\n".join(
        f"| `{r['table_name']}` | {'Detention facility segments' if r['table_name'] == 'detentions' else r['description']} | {r['row_count']:,} "
        f"| {r['column_count']} | {r['data_sources']} | {r['date_range']} |"
        for _, r in metadata.iterrows()
    )
    total_rows = int(metadata["row_count"].sum())
    n_tables = len(metadata)

    return f"""---
license: cc0-1.0
task_categories:
  - tabular-classification
  - tabular-regression
tags:
  - immigration
  - ice
  - enforcement
  - deportation
  - detention
  - foia
  - duckdb
  - legal
  - policy
  - government-data
pretty_name: ICE Enforcement Database
size_categories:
  - 10M<n<100M
---

# ICE Enforcement Database

A clean, queryable DuckDB database built from ICE enforcement data published by the [Deportation Data Project](https://law.ucla.edu/academics/centers/center-immigration-law-and-policy/deportation-data-project) (Berkeley Law / UCLA) via FOIA litigation.

**{total_rows:,} rows** across **{n_tables} tables** covering ICE arrests, detainers, detentions, removals, encounters, and custody decisions.

Combines two FOIA releases:
- **2023 release** (FY2012-FY2023): arrests, detentions, removals, RCA decisions
- **August 2026 cumulative release** (Oct 1, 2022 - Aug 6, 2026): arrests, detainers, detentions, removals, encounters

Every row has a `data_source` column (`release_2023` or `release_2026_08`). The August cumulative release supersedes older overlapping records; RCA remains historical through September 2023. This September 14, 2026 build reads original FOIA exports, not the publisher's separately processed derivative datasets.

Built with [ice-database](https://github.com/ian-nason/ice-database).

## Quick Start

### DuckDB CLI

```sql
INSTALL httpfs;
LOAD httpfs;
ATTACH 'https://huggingface.co/datasets/Nason/ice-database/resolve/main/ice.duckdb' AS ice (READ_ONLY);

-- Arrests by month
SELECT DATE_TRUNC('month', apprehension_date) AS month, COUNT(*) AS arrests
FROM ice.arrests
WHERE apprehension_date IS NOT NULL
GROUP BY 1 ORDER BY 1 DESC LIMIT 12;
```

### Python

```python
import duckdb
con = duckdb.connect(config={{"memory_limit": "128MiB", "threads": "1", "max_temp_directory_size": "0B"}})
try:
    con.execute("INSTALL httpfs; LOAD httpfs;")
    con.execute("ATTACH 'https://huggingface.co/datasets/Nason/ice-database/resolve/main/ice.duckdb' AS ice (READ_ONLY)")
    con.sql("SELECT * FROM ice._metadata").show()
finally:
    con.close()
```

Queries run on your machine using HTTP range requests. Transfer depends on columns and scans; a final LIMIT does not guarantee a small transfer. The memory setting above limits DuckDB buffers, not the entire process; larger queries may fail with spill disabled.

## Tables

| Table | Description | Rows | Cols | Sources | Date Range |
|-------|-------------|------|------|---------|------------|
{table_rows}

The card corrects the `detentions` label to **facility segments**. An existing database can still retain the legacy "Detention stays" description in `_metadata`; this card does not rewrite that database. Use the segment/stay distinction below regardless of the older embedded label.

## Key Features

### Linked Records
Tables share `unique_id` only within the same `data_source`; IDs are re-anonymized across releases. Always include the release in joins. `detentions` contains facility segments, not unique stays; use `v_detention_stays` for stays.

### Pre-built Views
- `v_arrest_to_detention` - Arrests joined to detention stays
- `v_enforcement_pipeline` - Full pipeline: arrest -> detention -> removal
- `v_daily_arrests` - Daily arrest counts by data source

### Multi-release Deduplication
Within-release duplicates are handled by the builder. Cross-release overlap is removed by time-window supersession, not by matching re-anonymized IDs: arrests by apprehension date, removals by departure date, and detentions by whether the stay was active on or after October 1, 2022. Older cumulative 2025/March 2026 releases are superseded. See the source repository for precise rules and missing/date-quality caveats.

## Data Source

[Deportation Data Project](https://law.ucla.edu/academics/centers/center-immigration-law-and-policy/deportation-data-project) (Berkeley Law / UCLA). Data obtained through FOIA litigation against ICE.

## License

Database build code: MIT. Underlying data: public domain (U.S. government records released via FOIA).

## GitHub

Full source code, build instructions, and example queries: [github.com/ian-nason/ice-database](https://github.com/ian-nason/ice-database)
"""


def main():
    parser = argparse.ArgumentParser(
        description="Upload ice.duckdb to Hugging Face"
    )
    parser.add_argument("--db", type=Path, default=Path("ice.duckdb"))
    parser.add_argument("--repo", default="Nason/ice-database")
    parser.add_argument("--token", help="HF token (or set HF_TOKEN env var)")
    parser.add_argument("--card-only", action="store_true",
                        help="Only (re)upload the dataset card README.md, not the .duckdb file")
    args = parser.parse_args()

    if not args.db.exists():
        print(f"Error: Database not found at {args.db}")
        sys.exit(1)

    api = HfApi(token=args.token)

    print(f"Creating dataset repo: {args.repo}")
    create_repo(args.repo, repo_type="dataset", exist_ok=True, token=args.token)

    print(f"Generating dataset card from {args.db}")
    card = generate_dataset_card(str(args.db))
    changelog = Path(__file__).parent / "CHANGELOG.md"
    if changelog.exists():
        card += "\n\n" + changelog.read_text()

    print("Uploading dataset card...")
    api.upload_file(
        path_or_fileobj=card.encode(),
        path_in_repo="README.md",
        repo_id=args.repo,
        repo_type="dataset",
    )

    if args.card_only:
        print("--card-only: skipping .duckdb upload")
    else:
        size_gb = args.db.stat().st_size / (1024**3)
        print(f"Uploading {args.db} ({size_gb:.1f} GB)...")
        api.upload_file(
            path_or_fileobj=str(args.db),
            path_in_repo="ice.duckdb",
            repo_id=args.repo,
            repo_type="dataset",
        )

    print(f"\nUploaded to https://huggingface.co/datasets/{args.repo}")
    print(
        f"\nUsers can now query remotely:\n"
        f"  ATTACH 'https://huggingface.co/datasets/{args.repo}/resolve/main/ice.duckdb'"
        f" AS ice (READ_ONLY);"
    )


if __name__ == "__main__":
    main()
