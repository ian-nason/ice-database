# Changelog

## 2026-09-14 — Data refresh (Deportation Data Project release of 2026-08-21)

- Rebuilt from the DDP's August 2026 ICE release (activity 2022-10-01 through
  2026-08-06), which is cumulative and fully supersedes the March 2026 and
  December 2025 releases. Total rows 22,030,619 → 23,568,538: `arrests`
  2,516,550 (release_2026_08 share 891,675), `detentions` 9,834,781,
  `removals` 3,868,035, `encounters` 3,065,104, `detainers` 740,601,
  `rca_decisions` 3,543,467 (unchanged, release_2023 only).
- `data_source` for the current release is now `release_2026_08`; the value
  `release_2026` no longer appears.
- New in the source: `arrests.city` (and `county`) for the 2022-10+ window
  (31% populated). ICE did not include `apprehension_type` in this release.
- Fix: the exact whole-row dedup of `encounters` (12,419 rows here; 12,097 in
  July) is now part of the build instead of a one-off repair, and validation
  asserts zero exact duplicates, view/arrest row parity, no negative
  durations, and that no superseded release remains.
- Harmonization: `Anonymized Unique Identifier`, `Stay Book Out Date Time` and
  `Detention Book In Date Time` headers now map onto `unique_id`,
  `stay_book_out_date` and `detention_book_in_date` (the July build carried a
  separate, mostly-null `stay_book_out_date_time` column).
- Builder recognises the DDP's abbreviated file names (ARS/DPR/DET/ENC/REM);
  `scripts/download_releases.sh` fetches both releases from their box.com
  links. DuckDB memory capped at 4 GB / 4 threads; `publish_to_hf.py --card-only`.
- Caveats unchanged: `unique_id` never links across releases; `detentions` is
  facility-segment level; DDP continues to flag the removals data as less
  reliable than the July 2025 release.

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
