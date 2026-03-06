-- ============================================================
-- ICE Enforcement Database — Example Queries
-- ============================================================
-- Run these against ice.duckdb with:
--   duckdb ice.duckdb < examples/query_examples.sql
-- Or remotely:
--   INSTALL httpfs; LOAD httpfs;
--   ATTACH 'https://huggingface.co/datasets/Nason/ice-database/resolve/main/ice.duckdb' AS ice (READ_ONLY);
-- ============================================================

-- 1. Arrests by month
SELECT
    DATE_TRUNC('month', apprehension_date) AS month,
    COUNT(*) AS arrests
FROM arrests
WHERE apprehension_date IS NOT NULL
GROUP BY 1
ORDER BY 1 DESC
LIMIT 24;

-- 2. Arrests by state (2025 release only — 2023 lacks this field)
SELECT
    apprehension_state AS state,
    COUNT(*) AS arrests
FROM arrests
WHERE apprehension_state IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC
LIMIT 15;

-- 3. Arrests by AOR (Area of Responsibility)
SELECT
    apprehension_aor AS aor,
    COUNT(*) AS arrests
FROM arrests
WHERE apprehension_aor IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC
LIMIT 15;

-- 4. Top citizenship countries (arrests)
SELECT
    citizenship_country,
    COUNT(*) AS arrests
FROM arrests
WHERE citizenship_country IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC
LIMIT 15;

-- 5. Criminal vs non-criminal arrests by month
SELECT
    DATE_TRUNC('month', apprehension_date) AS month,
    COUNT(*) AS total_arrests,
    COUNT(*) FILTER (WHERE final_program LIKE '%Criminal%') AS criminal,
    COUNT(*) FILTER (WHERE final_program NOT LIKE '%Criminal%'
                      AND final_program IS NOT NULL) AS non_criminal
FROM arrests
WHERE apprehension_date IS NOT NULL
GROUP BY 1
ORDER BY 1 DESC
LIMIT 12;

-- 6. Detainers by facility state
SELECT
    facility_state,
    COUNT(*) AS detainers
FROM detainers
WHERE facility_state IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC
LIMIT 15;

-- 7. Top detention facilities by number of stays
SELECT
    detention_facility AS facility,
    COUNT(*) AS stays,
    ROUND(MEDIAN(
        DATEDIFF('day', stay_book_in_date,
                 COALESCE(stay_book_out_date, CURRENT_DATE))
    ), 0) AS median_days
FROM detentions
WHERE detention_facility IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC
LIMIT 15;

-- 8. Currently detained population (no book-out date)
SELECT
    detention_facility AS facility,
    COUNT(*) AS currently_detained,
    ROUND(MEDIAN(
        DATEDIFF('day', stay_book_in_date, CURRENT_DATE)
    ), 0) AS median_days_detained
FROM detentions
WHERE stay_book_out_date IS NULL
  AND stay_book_in_date IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC
LIMIT 15;

-- 9. Detention release reasons
SELECT
    detention_release_reason,
    COUNT(*) AS n,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 1) AS pct
FROM detentions
WHERE detention_release_reason IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC
LIMIT 15;

-- 10. Detention length distribution
SELECT
    CASE
        WHEN days <= 7 THEN '0-7 days'
        WHEN days <= 30 THEN '8-30 days'
        WHEN days <= 90 THEN '31-90 days'
        WHEN days <= 180 THEN '91-180 days'
        WHEN days <= 365 THEN '181-365 days'
        ELSE '365+ days'
    END AS bucket,
    COUNT(*) AS stays
FROM (
    SELECT DATEDIFF('day', stay_book_in_date,
                    COALESCE(stay_book_out_date, CURRENT_DATE)) AS days
    FROM detentions
    WHERE stay_book_in_date IS NOT NULL
)
GROUP BY 1
ORDER BY MIN(days);

-- 11. Removals by month
SELECT
    DATE_TRUNC('month', departure_date) AS month,
    COUNT(*) AS removals
FROM removals
WHERE departure_date IS NOT NULL
GROUP BY 1
ORDER BY 1 DESC
LIMIT 24;

-- 12. Arrest-to-removal pipeline timing
SELECT
    DATE_TRUNC('month', apprehension_date) AS month,
    COUNT(*) AS total_arrests,
    COUNT(departure_date) AS resulted_in_removal,
    ROUND(100.0 * COUNT(departure_date) / COUNT(*), 1) AS removal_pct,
    ROUND(MEDIAN(days_to_removal), 0) AS median_days_to_removal
FROM v_enforcement_pipeline
WHERE apprehension_date IS NOT NULL
GROUP BY 1
ORDER BY 1 DESC
LIMIT 12;

-- 13. Daily arrest counts by data source
SELECT *
FROM v_daily_arrests
WHERE date >= DATE '2024-01-01'
ORDER BY date DESC
LIMIT 30;

-- 14. Arrest program breakdown
SELECT
    final_program,
    COUNT(*) AS arrests,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 1) AS pct
FROM arrests
WHERE final_program IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC
LIMIT 15;

-- 15. Data source coverage comparison
SELECT
    data_source,
    MIN(apprehension_date)::DATE AS earliest,
    MAX(apprehension_date)::DATE AS latest,
    COUNT(*) AS rows
FROM arrests
WHERE apprehension_date IS NOT NULL
GROUP BY 1
ORDER BY 1;
