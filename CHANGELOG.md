# Changelog

## 2026-07-06 — Full refresh + data-quality audit

Rebuilt from the Deportation Data Project's 2026 FOIA release (data through
2026-03-10) and repaired after an independent SQL-verified audit.

**Data changes**
- New `encounters` table (2,586,515 rows, release_2026 only).
- Release_2025 fully superseded by release_2026; release_2023 rows inside the
  2026 window (2022-10-01 onward) deleted to prevent double counting.
  Detention supersede keys on *stay* book-out, removing 17,970 previously
  double-counted boundary-spanning segments.
- 12,097 exact-duplicate encounters rows removed.
- Totals: 22,030,619 rows across 6 tables (was 17.8M across 5).

**Fixes**
- Views rewritten: `v_arrest_to_detention` and `v_enforcement_pipeline` now
  produce one row per arrest, matching the first detention stay / removal on
  or after the arrest within the same release (the old versions joined on
  `unique_id` alone, fanning out 3.1x with 20-27% negative durations). New
  `v_detention_stays` view collapses facility segments to stays.
- `removals.departure_date` header rename in the 2026 release handled
  (previously would load as all-NULL).

**Known caveats** (see README for the full list)
- `unique_id` never links across releases (re-anonymized per FOIA release).
- Detainers and encounters exist only from Oct 2022; `rca_decisions` ends
  Sep 2023.
- `arrests` demographics (citizenship, gender, birth year) exist only in
  release_2026 rows.
