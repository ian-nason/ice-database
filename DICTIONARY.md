# Data Dictionary

Source: [Deportation Data Project](https://deportationdata.org)

## arrests

ICE administrative arrests

Rows: 2,516,550

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| apprehension_date | TIMESTAMP | 0.0% | 2015-10-26 00:00:00 | Arrest date, joins arrests to detentions by person+date |
| apprehension_method | VARCHAR | 0.0% | Located |  |
| arrest_created_by | VARCHAR | 35.4% | (b)(6)(b)(7)(c) |  |
| case_id | VARCHAR | 37.4% | (b)(6)(b)(7)(c) | EID case identifier |
| subject_id | VARCHAR | 35.4% | (b)(6)(b)(7)(c) |  |
| alien_file_number | VARCHAR | 5.9% | (b)(6)(b)(7)(c) |  |
| unique_id | VARCHAR | 1.4% | f62520f6cfab8ad227a064a1e9e633d15c7ca3b7 | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023 or the latest cumulative release, e.g. release_2026_08) |
| aor | VARCHAR | 64.9% | Houston Area of Responsibility |  |
| apprehension_criminality | VARCHAR | 64.6% | 3 Other Immigration Violator |  |
| event_landmark | VARCHAR | 72.5% | ICE ERO NEWARK |  |
| state | VARCHAR | 68.8% | TEXAS |  |
| city | VARCHAR | 68.9% | NEWARK |  |
| birth_year | BIGINT | 64.6% | 2010 |  |
| case_category | VARCHAR | 65.6% | [8C] Excludable / Inadmissible - Administrative Final Order Issued |  |
| case_status | VARCHAR | 65.6% | 3-Voluntary Departure Confirmed |  |
| case_threat_level | DOUBLE | 87.6% | 3.0 |  |
| citizenship_country | VARCHAR | 64.6% | BRAZIL |  |
| departed_date | TIMESTAMP | 76.9% | 2023-03-29 00:00:00 |  |
| departure_country | VARCHAR | 76.9% | MEXICO |  |
| final_order_date | TIMESTAMP | 80.2% | 2023-03-27 00:00:00 |  |
| final_order_yes_no | VARCHAR | 65.6% | YES |  |
| final_program | VARCHAR | 64.6% | ERO Criminal Alien Program |  |
| final_program_group | VARCHAR | 64.6% | ICE |  |
| gender | VARCHAR | 64.6% | Male |  |

## detainers

Detainer requests issued to jails/prisons

Rows: 740,601

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| apprehension_date | TIMESTAMP | 74.0% | 2022-11-08 13:01:00 | Arrest date, joins arrests to detentions by person+date |
| apprehension_method | VARCHAR | 74.0% | CAP Local Incarceration |  |
| biometric_match_yes_no | VARCHAR | 18.6% | YES |  |
| birth_country | VARCHAR | 0.0% | EL SALVADOR |  |
| birth_year | DOUBLE | 0.0% | 1989.0 |  |
| case_category | VARCHAR | 48.3% | [16] Reinstated Final Order |  |
| case_status | VARCHAR | 48.3% | 8-Excluded/Removed - Inadmissibility |  |
| citizenship_country | VARCHAR | 0.0% | EL SALVADOR |  |
| departed_date | TIMESTAMP | 67.5% | 2022-12-02 00:00:00 |  |
| departure_country | VARCHAR | 67.5% | HONDURAS |  |
| deportation_ordered_yes_no | VARCHAR | 18.6% | NO |  |
| detainer_lift_reason | VARCHAR | 27.1% | Booked into Detention |  |
| detainer_prepared_threat_level | DOUBLE | 9.5% | 1.0 |  |
| detainer_prepared_date | TIMESTAMP | 0.0% | 2022-10-18 00:00:00 |  |
| detainer_prepared_criminality | VARCHAR | 0.0% | 1 Convicted Criminal |  |
| detainer_type | VARCHAR | 0.0% | I247A - Immigration Detainer - Immigration Detainer - Notice of Action |  |
| detention_facility | VARCHAR | 0.0% | WASHINGTON COUNTY JAIL |  |
| detention_facility_code | VARCHAR | 0.0% | WASHCUT | Facility identifier for detention location |
| entry_date | TIMESTAMP | 86.7% | 2022-10-10 00:00:00 |  |
| entry_status | VARCHAR | 25.5% | Not  Applicable |  |
| aor | VARCHAR | 18.0% | Salt Lake City Area of Responsibility |  |
| city | VARCHAR | 0.1% | HURRICANE |  |
| state | VARCHAR | 0.1% | UTAH |  |
| felon | VARCHAR | 0.2% | Not an Aggravated Felon |  |
| final_order_date | TIMESTAMP | 67.5% | 2022-07-25 00:00:00 |  |
| final_order_yes_no | VARCHAR | 48.3% | YES |  |
| tod_final_program | VARCHAR | 0.0% | ERO Criminal Alien Program |  |
| gender | VARCHAR | 0.0% | Male |  |
| msc_charge | VARCHAR | 73.6% | Burglary |  |
| msc_charge_code | VARCHAR | 73.6% | 2299 |  |
| msc_charge_date | TIMESTAMP | 73.6% | 2021-02-22 00:00:00 |  |
| msc_conviction_date | TIMESTAMP | 73.6% | 2022-05-27 00:00:00 |  |
| sentence_days | DOUBLE | 91.6% | 180.0 |  |
| sentence_months | DOUBLE | 93.9% | 70.0 |  |
| sentence_years | DOUBLE | 93.7% | 1.0 |  |
| order_to_show_cause_served_yes_no | VARCHAR | 18.6% | NO |  |
| port_of_departure | VARCHAR | 67.5% | ALEXANDRIA INTERNATIONAL AIRPORT, POE |  |
| processing_disposition | VARCHAR | 0.0% | REINSTATEMENT OF DEPORT ORDER I-871 |  |
| resume_custody_yes_no | VARCHAR | 0.0% | NO |  |
| statements_made_yes_no | VARCHAR | 18.6% | NO |  |
| toa_case_category | VARCHAR | 85.4% | [8C] Excludable / Inadmissible - Administrative Final Order Issued |  |
| toa_case_category_code | VARCHAR | 85.4% | 8A |  |
| alien_file_number | VARCHAR | 12.0% | (b)(6), (b)(7)(c) |  |
| unique_id | VARCHAR | 12.0% | d152302048050cc4438df7d3386b8f2b3a4e15ab | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2026_08 | Release identifier (release_2023 or the latest cumulative release, e.g. release_2026_08) |

## detentions

Detention stays (book-in to book-out)

Rows: 9,834,781

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| detention_id | VARCHAR | 30.2% | (b)(6)(b)(7)(c) |  |
| case_id | VARCHAR | 31.0% | (b)(6)(b)(7)(c) | EID case identifier |
| subject_id | VARCHAR | 30.2% | (b)(6)(b)(7)(c) |  |
| stay_book_in_date | TIMESTAMP | 0.0% | 2012-02-25 00:00:00 | Detention start date |
| detention_book_in_date | TIMESTAMP | 0.0% | 2012-03-05 00:00:00 |  |
| detention_facility | VARCHAR | 0.0% | MONROE COUNTY DETENTION-DORM |  |
| detention_facility_code | VARCHAR | 0.0% | MONROMI | Facility identifier for detention location |
| detention_book_out_date | TIMESTAMP | 0.7% | 2012-03-19 00:00:00 |  |
| detention_release_reason | VARCHAR | 0.7% | Transferred |  |
| stay_book_out_date | TIMESTAMP | 1.8% | 2012-03-21 00:00:00 |  |
| stay_release_reason | VARCHAR | 1.8% | U.S. Marshals or other agency (explain in Detention Comments) |  |
| religion | VARCHAR | 97.2% | Catholic |  |
| marital | VARCHAR | 0.7% | Single |  |
| gender | VARCHAR | 0.0% | Male |  |
| ethnicity | VARCHAR | 53.3% | Hispanic Origin |  |
| alien_file_number | VARCHAR | 0.5% | (b)(6)(b)(7)(c) |  |
| birth_year | DOUBLE | 0.0% | 1962.0 |  |
| entry_status | VARCHAR | 5.2% | PWA Mexico |  |
| bond_posted_date | TIMESTAMP | 87.4% | 2011-12-02 00:00:00 |  |
| bond_posted_amount | DOUBLE | 87.4% | 1500.0 |  |
| initial_bond_set_amount | DOUBLE | 86.1% | 1500.0 |  |
| case_status | VARCHAR | 1.0% | 8-Excluded/Removed - Inadmissibility |  |
| case_category | VARCHAR | 1.0% | [16] Reinstated Final Order |  |
| final_order_yes_no | VARCHAR | 1.0% | YES |  |
| final_order_date | TIMESTAMP | 30.9% | 2012-03-05 00:00:00 |  |
| departed_date | TIMESTAMP | 30.4% | 2012-12-04 00:00:00 |  |
| departure_country | VARCHAR | 30.5% | MEXICO |  |
| case_threat_level | DOUBLE | 55.7% | 1.0 |  |
| charge | VARCHAR | 53.0% | ALIEN PRESENT WITHOUT ADMISSION OR PAROLE - (PWAs) |  |
| charge_code | VARCHAR | 53.0% | I6A |  |
| charge_section_code | VARCHAR | 53.0% | 212a6Ai |  |
| unique_id | VARCHAR | 0.5% | 4e30bfd2a1bd17e6e0f08358114bb32750028550 | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023 or the latest cumulative release, e.g. release_2026_08) |
| book_in_criminality | VARCHAR | 69.8% | 3 Other Immigration Violator |  |
| citizenship_country | VARCHAR | 69.8% | CUBA |  |
| entry_date | TIMESTAMP | 83.0% | 2022-09-18 00:00:00 |  |
| felon | VARCHAR | 84.3% | Not an Aggravated Felon |  |
| final_charge | VARCHAR | 77.0% | ALIEN PRESENT WITHOUT ADMISSION OR PAROLE - (PWAs) |  |
| apprehension_final_program | VARCHAR | 70.8% | Border Patrol |  |
| msc_charge | VARCHAR | 90.5% | Assault |  |
| apprehension_final_program_group | VARCHAR | 70.8% | CBP |  |

## encounters

ICE encounters with individuals

Rows: 3,065,104

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| birth_year | DOUBLE | 0.1% | 2014.0 |  |
| case_category | VARCHAR | 50.0% | [8B] Excludable / Inadmissible - Under Adjudication by IJ |  |
| case_status | VARCHAR | 50.0% | ACTIVE |  |
| citizenship_country | VARCHAR | 0.0% | BRAZIL |  |
| departed_date | TIMESTAMP | 75.5% | 2024-03-05 00:00:00 |  |
| departure_country | VARCHAR | 75.6% | MEXICO |  |
| encounter_criminality | VARCHAR | 0.0% | 3 Other Immigration Violator |  |
| event_date | TIMESTAMP | 0.0% | 2023-04-11 08:56:00 |  |
| event_type | VARCHAR | 0.0% | CAP Local |  |
| final_order_date | TIMESTAMP | 75.4% | 2025-03-28 00:00:00 |  |
| final_order_yes_no | VARCHAR | 50.0% | NO |  |
| final_program | VARCHAR | 0.0% | ERO Criminal Alien Program |  |
| final_program_group | VARCHAR | 0.0% | ICE |  |
| gender | VARCHAR | 0.0% | M |  |
| event_landmark | VARCHAR | 56.4% | ELIZABETH PD |  |
| lead_event_type | VARCHAR | 0.0% | Not applicable |  |
| lead_source | VARCHAR | 86.6% | USMS Referral (US Marshals Service) |  |
| processing_disposition | VARCHAR | 0.1% | Not Amenable to Removal |  |
| responsible_aor | VARCHAR | 3.5% | Newark Area of Responsibility |  |
| responsible_site | VARCHAR | 0.0% | NEWARK, NJ, DOCKET CONTROL OFFICE |  |
| alien_file_number | VARCHAR | 10.5% | (b)(6), (b)(7)(c) |  |
| unique_id | VARCHAR | 10.5% | 194850edf37560ab81beb9bd505e3c91bebfcd2b | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2026_08 | Release identifier (release_2023 or the latest cumulative release, e.g. release_2026_08) |

## rca_decisions

Release/custody assessment decision history

Rows: 3,543,467

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| rca_aor | VARCHAR | 0.0% | BAL |  |
| rca_dco | VARCHAR | 0.0% | BAL |  |
| a_number | VARCHAR | 0.3% | b(6), b(7)(c) |  |
| subj_id | VARCHAR | 10.0% | b(6), b(7)(c) |  |
| last_name | VARCHAR | 0.0% | b(6), b(7)(c) |  |
| first_name | VARCHAR | 0.0% | b(6), b(7)(c) |  |
| alert_code | VARCHAR | 56.5% | 3 |  |
| active_inactive | VARCHAR | 0.0% | Active |  |
| submission_date | TIMESTAMP | 16.1% | 2012-08-28 00:00:00 |  |
| status_code | VARCHAR | 26.1% | C |  |
| risk_to_public_safety | VARCHAR | 16.1% | Low |  |
| risk_of_flight | VARCHAR | 16.1% | High |  |
| special_vulnerability | VARCHAR | 17.9% | NONE |  |
| rca_case_number | VARCHAR | 68.6% | b(7)(e) |  |
| case_cat_at_rca_decision | VARCHAR | 68.6% | 8C |  |
| fo_at_rca_decision | VARCHAR | 0.0% | Y |  |
| fo_date_at_rca_decision | TIMESTAMP | 70.4% | 2012-02-27 00:00:00 |  |
| removal_likely_at_rca_decision | VARCHAR | 89.4% | Y |  |
| man_det_per_stat_alleg | VARCHAR | 31.4% | N |  |
| rca_decision_type | VARCHAR | 0.0% | Detain/Release  |  |
| rca_recommendation | VARCHAR | 0.0% | Supervisor to Determine - Detain or Release on Community Supervision |  |
| rca_bond_recommendation | DOUBLE | 93.6% | 9000.0 |  |
| officer_id | VARCHAR | 16.1% | b(6), b(7)(c) |  |
| officer_agree_disagree | VARCHAR | 16.1% | Not Applicable, Supervisor to Determine |  |
| supervisor_id | VARCHAR | 1.8% | b(6), b(7)(c) |  |
| supervisor_agree_disagree | VARCHAR | 0.0% | Not Applicable, Supervisor to Determine |  |
| rca_final_decision | VARCHAR | 0.0% | Detain in the Custody of This Service |  |
| final_bond_amount | DOUBLE | 98.0% | 18000.0 |  |
| rca_decision_date | TIMESTAMP | 0.0% | 2012-08-28 00:00:00 |  |
| rca_scoring_ver | DOUBLE | 16.1% | 1.2 |  |
| spec_vuln_ver | DOUBLE | 16.1% | 1.0 |  |
| man_det_ver | DOUBLE | 91.9% | 1.0 |  |
| disc_infr_ver | DOUBLE | 99.8% | 1.0 |  |
| fiscal_year_code | BIGINT | 0.0% | 2013 |  |
| fiscal_quarter_name | VARCHAR | 0.0% | Q4 |  |
| unique_id | VARCHAR | 0.3% | 00001ed059f30ad45f361ac3e86087cc9854a1fb | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023 or the latest cumulative release, e.g. release_2026_08) |
| special_vulnerability_comments | VARCHAR | 99.6% | b(6), b(7)(c) |  |
| reason_removal_unlikely_at_rca_decision | VARCHAR | 99.4% | Prosecutorial Discretion |  |
| officer_comments | VARCHAR | 97.3% | b(6), b(7)(c) |  |
| supervisor_comments | VARCHAR | 96.7% | b(6), b(7)(c) |  |
| sujb_id | VARCHAR | 90.0% | (b)(6),(b)(7)(c) |  |

## removals

Deportation/removal records

Rows: 3,868,035

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| departure_date | TIMESTAMP | 0.0% | 2013-01-22 00:00:00 | Removal/departure date |
| port_of_departure | VARCHAR | 0.0% | HOUSTON, TX, POE |  |
| departure_country | VARCHAR | 0.0% | EL SALVADOR |  |
| case_status | VARCHAR | 0.0% | 8-Excluded/Removed - Inadmissibility |  |
| case_category | VARCHAR | 0.0% | [8F] Expedited Removal |  |
| final_order_yes_no | VARCHAR | 0.0% | YES |  |
| final_order_date | TIMESTAMP | 10.8% | 1990-02-22 00:00:00 |  |
| case_id | VARCHAR | 32.1% | (b)(6),(b)(7)(c) | EID case identifier |
| gender | VARCHAR | 0.0% | Male |  |
| birth_country | VARCHAR | 32.1% | MEXICO |  |
| citizenship_country | VARCHAR | 0.0% | EL SALVADOR |  |
| birth_year | DOUBLE | 0.0% | 1970.0 |  |
| alien_file_number | VARCHAR | 0.6% | (b)(6),(b)(7)(c) |  |
| entry_status | VARCHAR | 1.8% | PWA Mexico |  |
| entry_date | TIMESTAMP | 25.6% | 2012-04-13 00:00:00 |  |
| msc_charge | VARCHAR | 52.4% | Traffic Offense |  |
| msc_charge_date | TIMESTAMP | 54.5% | 2012-07-26 00:00:00 |  |
| msc_charge_code | VARCHAR | 52.4% | 5499 |  |
| msc_conviction_date | TIMESTAMP | 52.4% | 2007-04-02 00:00:00 |  |
| msc_criminal_charge_status | VARCHAR | 52.4% | Convicted |  |
| case_threat_level | DOUBLE | 52.4% | 1.0 |  |
| processing_disposition_code | VARCHAR | 32.1% | NTA/DT |  |
| processing_disposition | VARCHAR | 32.1% | REINSTATEMENT OF DEPORT ORDER I-871 |  |
| current_program | VARCHAR | 32.8% | Detention and Deportation |  |
| apprehension_date | TIMESTAMP | 1.1% | 2007-07-20 00:00:00 | Arrest date, joins arrests to detentions by person+date |
| charge_section_code | VARCHAR | 32.4% | 212a6Ai |  |
| charge_code | VARCHAR | 32.4% | I6A |  |
| unique_id | VARCHAR | 0.6% | d7e01d84275800c05eff1b0752fa989889096231 | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023 or the latest cumulative release, e.g. release_2026_08) |
| apprehension_state | VARCHAR | 90.9% | ARIZONA |  |
| apprehension_city | VARCHAR | 91.1% | Phoenix |  |
| toa_case_category | VARCHAR | 98.1% | [8A] Excludable / Inadmissible - Hearing Not Commenced |  |
| case_criminality | VARCHAR | 67.9% | 3 Other Immigration Violator |  |
| docket_aor | VARCHAR | 67.9% | Houston Area of Responsibility |  |
| final_charge_code | VARCHAR | 67.9% | I7A1 |  |
| final_charge_section | VARCHAR | 67.9% | 212a7AiI |  |
| final_program | VARCHAR | 67.9% | BP |  |
| final_program_code | VARCHAR | 67.9% | Border Patrol |  |
| latest_apprehension_program_code | VARCHAR | 68.2% | BP |  |
| latest_apprehension_program | VARCHAR | 68.2% | Border Patrol |  |
| prior_deport_yes_no | VARCHAR | 67.9% | NO |  |
| progrocessing_disposition | VARCHAR | 67.9% | Expedited Removal with Credible Fear |  |
| arresting_agency | VARCHAR | 67.9% | CBP |  |

## v_arrest_to_detention

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| apprehension_date | TIMESTAMP | 0.0% | 2016-02-12 00:00:00 | Arrest date, joins arrests to detentions by person+date |
| apprehension_method | VARCHAR | 0.0% | CAP Local Incarceration |  |
| arrest_created_by | VARCHAR | 35.4% | (b)(6)(b)(7)(c) |  |
| case_id | VARCHAR | 37.4% | (b)(6)(b)(7)(c) | EID case identifier |
| subject_id | VARCHAR | 35.4% | (b)(6)(b)(7)(c) |  |
| alien_file_number | VARCHAR | 5.9% | (b)(6)(b)(7)(c) |  |
| unique_id | VARCHAR | 1.4% | f65e357959520b00d306e01a74fdec2d45f57330 | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023 or the latest cumulative release, e.g. release_2026_08) |
| aor | VARCHAR | 64.9% | Dallas Area of Responsibility |  |
| apprehension_criminality | VARCHAR | 64.6% | 3 Other Immigration Violator |  |
| event_landmark | VARCHAR | 72.5% | SLC GENERAL AREA, NON-SPECIFIC |  |
| state | VARCHAR | 68.8% | UTAH |  |
| city | VARCHAR | 68.9% | DALLAS |  |
| birth_year | BIGINT | 64.6% | 1982 |  |
| case_category | VARCHAR | 65.6% | [3] Deportable - Administratively Final Order |  |
| case_status | VARCHAR | 65.6% | ACTIVE |  |
| case_threat_level | DOUBLE | 87.6% | 1.0 |  |
| citizenship_country | VARCHAR | 64.6% | RWANDA |  |
| departed_date | TIMESTAMP | 76.9% | 2024-11-18 00:00:00 |  |
| departure_country | VARCHAR | 76.9% | PERU |  |
| final_order_date | TIMESTAMP | 80.2% | 2024-09-07 00:00:00 |  |
| final_order_yes_no | VARCHAR | 65.6% | NO |  |
| final_program | VARCHAR | 64.6% | Mobile Criminal Alien Team |  |
| final_program_group | VARCHAR | 64.6% | ICE |  |
| gender | VARCHAR | 64.6% | Male |  |
| stay_book_in_date | TIMESTAMP | 21.2% | 2016-02-12 00:00:00 | Detention start date |
| stay_book_out_date | TIMESTAMP | 23.4% | 2016-06-15 00:00:00 |  |
| stay_release_reason | VARCHAR | 23.4% | Removed |  |
| initial_detention_facility | VARCHAR | 21.2% | SANTA ANA DRO HOLDROOM |  |
| days_arrest_to_detention | BIGINT | 21.2% | 0 |  |
| days_in_detention | BIGINT | 23.4% | 124 |  |

## v_daily_arrests

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| date | DATE | 0.0% | 2011-10-01 |  |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023 or the latest cumulative release, e.g. release_2026_08) |
| arrest_count | BIGINT | 0.0% | 142 |  |

## v_detention_stays

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unique_id | VARCHAR | 0.3% | bba483a9b8f58aabe1e8d33cee4569071461983e | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023 or the latest cumulative release, e.g. release_2026_08) |
| stay_book_in_date | TIMESTAMP | 0.0% | 2012-03-07 00:00:00 | Detention start date |
| stay_book_out_date | TIMESTAMP | 1.3% | 2012-07-03 00:00:00 |  |
| stay_release_reason | VARCHAR | 1.3% | Removed |  |
| initial_detention_facility | VARCHAR | 0.0% | RIO GRANDE VALLEY STAGING |  |
| facility_segments | BIGINT | 0.0% | 1 |  |

## v_enforcement_pipeline

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unique_id | VARCHAR | 1.4% | f62632d6844d95278b4cb8a7fe4c5a899adcbfe9 | Anonymized person ID, links across arrests, detainers, detentions, removals |
| apprehension_date | TIMESTAMP | 0.0% | 2015-10-18 00:00:00 | Arrest date, joins arrests to detentions by person+date |
| arrest_source | VARCHAR | 0.0% | release_2023 |  |
| stay_book_in_date | TIMESTAMP | 21.2% | 2015-12-10 00:00:00 | Detention start date |
| stay_book_out_date | TIMESTAMP | 23.4% | 2016-07-12 00:00:00 |  |
| detention_facility | VARCHAR | 21.2% | SANTA ANA DRO HOLDROOM |  |
| departure_date | TIMESTAMP | 33.8% | 2017-05-16 00:00:00 | Removal/departure date |
| removal_country | VARCHAR | 33.8% | MEXICO |  |
| days_to_detention | BIGINT | 21.2% | 0 |  |
| days_detained | BIGINT | 23.4% | 181 |  |
| days_to_removal | BIGINT | 33.8% | 523 |  |
