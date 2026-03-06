# ICE Enforcement Database

A clean, queryable DuckDB database built from ICE enforcement data published by the [Deportation Data Project](https://law.ucla.edu/academics/centers/center-immigration-law-and-policy/deportation-data-project) (Berkeley Law / UCLA) via FOIA litigation.

**17.8M+ rows** across **5 tables** covering ICE arrests, detainers, detentions, removals, and custody decisions from FY2012 through October 2025.

## Data Sources

Two FOIA releases are combined and deduplicated:

| Release | Coverage | Tables |
|---------|----------|--------|
| 2023 FOIA litigation | FY2012 - FY2023 | arrests, detentions, removals, rca_decisions |
| 2025 settlement | Sep 2023 - Oct 2025 | arrests, detainers, detentions |

Every row has a `data_source` column (`release_2023` or `release_2025`). Where both releases overlap, records are deduplicated with the richer 2025 data preferred.

## Tables

| Table | Rows | Cols | Description |
|-------|------|------|-------------|
| `detentions` | 8,944,408 | 41 | Detention stays (book-in to book-out) |
| `rca_decisions` | 3,543,467 | 42 | Release/custody assessment decision history |
| `removals` | 2,771,219 | 29 | Deportation/removal records |
| `arrests` | 2,168,784 | 25 | ICE administrative arrests |
| `detainers` | 396,306 | 63 | Detainer requests issued to jails/prisons |

Tables share a `unique_id` field for tracing individuals across the enforcement pipeline.

## Quick Start (Remote Query)

No download needed. DuckDB uses HTTP range requests to fetch only the pages your query touches.

```sql
INSTALL httpfs;
LOAD httpfs;
ATTACH 'https://huggingface.co/datasets/Nason/ice-database/resolve/main/ice.duckdb' AS ice (READ_ONLY);

-- Monthly arrests
SELECT DATE_TRUNC('month', apprehension_date) AS month, COUNT(*) AS arrests
FROM ice.arrests
WHERE apprehension_date IS NOT NULL
GROUP BY 1 ORDER BY 1 DESC LIMIT 12;

-- Detention duration distribution
SELECT
    CASE
        WHEN days <= 7 THEN '0-7 days'
        WHEN days <= 30 THEN '8-30 days'
        WHEN days <= 90 THEN '31-90 days'
        WHEN days <= 365 THEN '91-365 days'
        ELSE '365+ days'
    END AS bucket,
    COUNT(*) AS stays
FROM (
    SELECT DATEDIFF('day', stay_book_in_date, stay_book_out_date) AS days
    FROM ice.detentions
    WHERE stay_book_in_date IS NOT NULL AND stay_book_out_date IS NOT NULL
)
GROUP BY 1 ORDER BY MIN(days);
```

See [`examples/query_examples.sql`](examples/query_examples.sql) for more.

## Build from Source

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
# 1. Place ICE xlsx files in data/raw/
#    data/raw/release_2023/  (30 xlsx files from 2023 FOIA release)
#    data/raw/release_2025/  (3 xlsx files from Dec 2025 settlement)

# 2. Build the database
uv run python build_database.py

# 3. (Optional) Upload to Hugging Face
uv run python publish_to_hf.py --token hf_YOUR_TOKEN
```

The build reads all xlsx files, auto-detects header rows (skipping FOUO preambles), normalizes column names, harmonizes schemas across releases, deduplicates overlapping records, and creates pre-built analysis views.

## Pre-built Views

| View | Description |
|------|-------------|
| `v_arrest_to_detention` | Arrests joined to detention stays with duration |
| `v_enforcement_pipeline` | Full pipeline: arrest -> detention -> removal |
| `v_daily_arrests` | Daily arrest counts by data source |

## License

Build code: MIT. Underlying data: public domain (U.S. government records released via FOIA).
