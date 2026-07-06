# ICE Enforcement Database

A clean, queryable DuckDB database built from ICE enforcement data published by the [Deportation Data Project](https://law.ucla.edu/academics/centers/center-immigration-law-and-policy/deportation-data-project) (Berkeley Law / UCLA) via FOIA litigation.

**22M+ rows** across **6 tables** covering ICE arrests, detainers, detentions, removals, encounters, and custody decisions from FY2012 through March 10, 2026.

## Data Sources

Two FOIA releases are combined:

| Release | Coverage | Tables |
|---------|----------|--------|
| 2023 FOIA litigation | FY2012 - Sep 30, 2022 (after supersede, see below) | arrests, detentions, removals, rca_decisions |
| 2026 release | Oct 1, 2022 - Mar 10, 2026 | arrests, detainers, detentions, removals, encounters |

Every row has a `data_source` column (`release_2023` or `release_2026`).

**How overlap is handled (supersede):** the 2026 release cumulatively covers activity from 2022-10-01 onward, overlapping the 2023 release's final year. Because rows cannot be matched across releases (see below), older-release rows inside the 2026 window are deleted wholesale: arrests by apprehension date, removals by departure date, and detentions by whether the *stay* was active on or after 2022-10-01. An earlier 2025 settlement release is fully contained in the 2026 window and was superseded entirely.

## Tables

| Table | Rows | Description |
|-------|------|-------------|
| `detentions` | 9,288,543 | Detention **facility segments** (~2 per stay; see caveats) |
| `removals` | 3,680,770 | Deportation/removal records |
| `rca_decisions` | 3,543,467 | Release/custody assessment decisions (release_2023 only, through Sep 2023) |
| `encounters` | 2,586,515 | ICE encounters (release_2026 only, Oct 2022+) |
| `arrests` | 2,334,315 | ICE administrative arrests |
| `detainers` | 597,009 | Detainer requests (release_2026 only, Oct 2022+) |

(Row counts as of the July 2026 build; `_metadata` inside the database is authoritative.)

## Researcher caveats — read before publishing numbers

1. **`unique_id` does NOT link across releases.** IDs are re-anonymized in every FOIA release; zero IDs are shared between `release_2023` and `release_2026`. Person histories cannot cross 2022-10-01, and re-arrest/recidivism rates near that boundary are structurally understated. Within a single release, linkage works well (81-85% of arrest IDs resolve in detentions).
2. **`detentions` is facility-segment level, not stay level.** A stay that moves between facilities has one row per facility. `COUNT(*)` overstates detention stays roughly 2x; aggregate to `(unique_id, stay_book_in_date)` or use the `v_detention_stays` view.
3. **Some columns exist in only one release.** `arrests.citizenship_country`, `gender`, and `birth_year` are populated only in `release_2026` (nothing before Oct 2022); `removals.apprehension_date` is release_2023-only while release_2026 has `latest_apprehension_date` (different semantics). Check per-release null rates in `_columns` before trending any column across the boundary.
4. **Coverage windows differ by table.** Arrests and removals are continuous Oct 2011 - Mar 2026. Detainers and encounters exist only from Oct 2022. `rca_decisions` ends Sep 2023. There is no pre-FY2023 detainer baseline in this data.
5. **Secondary dates contain source garbage** (years 0199-8017 in `entry_date`, `msc_charge_date`, `final_order_date`, etc.). Primary event dates (apprehension, departure, book-in/out) are nearly clean. Clamp secondary dates to 1990-2026 before computing intervals.
6. **Redacted ID columns are unusable.** `case_id`, `subject_id`, `alien_file_number`, and `a_number` contain only FOIA redaction strings like `(b)(6)(b)(7)(c)`. The only working key is `unique_id`.
7. **Fully-redacted duplicate rows remain in `arrests`** (~10k rows with NULL `unique_id` that are byte-identical). They may be distinct real events that redaction made indistinguishable; we deliberately did not delete them.

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

-- Detention duration distribution (stay level, not segment level)
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
    SELECT DATEDIFF('day', stay_book_in_date::DATE, stay_book_out_date::DATE) AS days
    FROM ice.v_detention_stays
    WHERE stay_book_in_date IS NOT NULL AND stay_book_out_date IS NOT NULL
)
GROUP BY 1 ORDER BY MIN(days);
```

See [`examples/query_examples.sql`](examples/query_examples.sql) for more.

## Pre-built Views

| View | Description |
|------|-------------|
| `v_detention_stays` | Detentions collapsed to one row per stay (use this for stay counts/durations) |
| `v_arrest_to_detention` | One row per arrest, matched to the first detention stay on/after the arrest within the same release |
| `v_enforcement_pipeline` | One row per arrest: arrest -> first detention stay -> first removal, date-constrained, same release |
| `v_daily_arrests` | Daily arrest counts by data source |

The join views match within `data_source` and require the detention/removal to occur on or after the arrest date, so durations are non-negative by construction. Arrests with no subsequent detention/removal in the same release keep NULL columns — remember that pipeline completion rates are lower bounds near release boundaries (caveat 1).

## Build from Source

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
# 1. Place ICE xlsx files in data/raw/
#    data/raw/release_2023/  (30 xlsx files from 2023 FOIA release)
#    data/raw/release_2026/  (xlsx files from the 2026 release)

# 2. Build the database
uv run python build_database.py

# 3. (Optional) Upload to Hugging Face
uv run python publish_to_hf.py --token hf_YOUR_TOKEN
```

The build reads all xlsx files, auto-detects header rows (skipping FOUO preambles), normalizes column names, harmonizes schemas across releases, deduplicates within releases, applies the cross-release supersede, and creates the analysis views.

## License

Build code: MIT. Underlying data: public domain (U.S. government records released via FOIA).
