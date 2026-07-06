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
        f"| `{r['table_name']}` | {r['description']} | {r['row_count']:,} "
        f"| {r['column_count']} | {r['data_sources']} | {r['date_range']} |"
        for _, r in metadata.iterrows()
    )
    total_rows = int(metadata["row_count"].sum())
    n_tables = len(metadata)

    return f"""---
license: mit
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

**{total_rows:,} rows** across **{n_tables} tables** covering ICE arrests, detainers, detentions, removals, and custody decisions.

Combines two FOIA releases:
- **2023 release** (FY2012-FY2023): arrests, detentions, removals, RCA decisions
- **2025 settlement release** (Sep 2023 - Oct 2025): arrests, detainers, detentions

Every row has a `data_source` column (`release_2023` or `release_2025`) so you can filter by release. Overlapping records are deduplicated, preferring the richer 2025 data.

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
con = duckdb.connect()
con.sql("INSTALL httpfs; LOAD httpfs;")
con.sql(\\\"\\\"\\\"
    ATTACH 'https://huggingface.co/datasets/Nason/ice-database/resolve/main/ice.duckdb'
    AS ice (READ_ONLY)
\\\"\\\"\\\")
con.sql("SELECT * FROM ice._metadata").show()
```

DuckDB uses HTTP range requests, so only the pages needed for your query are downloaded.

## Tables

| Table | Description | Rows | Cols | Sources | Date Range |
|-------|-------------|------|------|---------|------------|
{table_rows}

## Key Features

### Linked Records
Tables share a `unique_id` field for tracing individuals across the enforcement pipeline: arrests -> detainers -> detentions -> removals.

### Pre-built Views
- `v_arrest_to_detention` - Arrests joined to detention stays
- `v_enforcement_pipeline` - Full pipeline: arrest -> detention -> removal
- `v_daily_arrests` - Daily arrest counts by data source

### Multi-release Deduplication
Where both releases cover the same period, records are deduplicated on key fields (unique_id + date + facility) with the richer 2025 release preferred.

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
