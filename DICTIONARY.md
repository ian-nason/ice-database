# Data Dictionary

Source: [Deportation Data Project](https://deportationdata.org)

## arrests

ICE administrative arrests

Rows: 2,168,784

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| apprehension_date | TIMESTAMP | 0.0% | 2011-10-13 00:00:00 | Arrest date, joins arrests to detentions by person+date |
| apprehension_method | VARCHAR | 0.0% | Inspections |  |
| arrest_created_by | VARCHAR | 17.3% | (b)(6)(b)(7)(c) |  |
| case_id | VARCHAR | 2.8% | (b)(6)(b)(7)(c) | EID case identifier |
| subject_id | VARCHAR | 0.0% | (b)(6)(b)(7)(c) |  |
| alien_file_number | VARCHAR | 1.1% | (b)(6)(b)(7)(c) |  |
| unique_id | VARCHAR | 1.1% | 6c7ebdebf9bb953d46703e79eee499a46c79425b | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023 or release_2025) |
| apprehension_state | VARCHAR | 85.4% | VIRGINIA |  |
| apprehension_aor | VARCHAR | 83.0% | Washington Area of Responsibility |  |
| final_program | VARCHAR | 82.7% | ERO Criminal Alien Program |  |
| final_program_group | VARCHAR | 82.7% | ICE |  |
| apprehension_criminality | VARCHAR | 82.7% | 2 Pending Criminal Charges |  |
| case_status | VARCHAR | 83.2% | 3-Voluntary Departure Confirmed |  |
| case_category | VARCHAR | 83.2% | [8C] Excludable / Inadmissible - Administrative Final Order Issued |  |
| departed_date | TIMESTAMP | 89.2% | 2025-05-29 00:00:00 |  |
| departure_country | VARCHAR | 89.2% | JAMAICA |  |
| final_order_yes_no | VARCHAR | 83.2% | NO |  |
| final_order_date | TIMESTAMP | 89.5% | 2024-02-22 00:00:00 |  |
| birth_year | DOUBLE | 82.7% | 2005.0 |  |
| citizenship_country | VARCHAR | 82.7% | JAMAICA |  |
| gender | VARCHAR | 82.7% | Male |  |
| apprehension_site_landmark | VARCHAR | 83.1% | CULPEPER COUNTY JAIL - VA |  |

## detainers

Detainer requests issued to jails/prisons

Rows: 396,306

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| detainer_prepare_date | TIMESTAMP | 0.0% | 2025-09-18 00:00:00 |  |
| facility_state | VARCHAR | 0.1% | NEW YORK |  |
| facility_aor | VARCHAR | 20.0% | New York City Area of Responsibility |  |
| port_of_departure | VARCHAR | 73.9% | SAN ANTONIO, TX, POE |  |
| departure_country | VARCHAR | 73.9% | HONDURAS |  |
| departed_date | TIMESTAMP | 73.9% | 2023-12-18 00:00:00 |  |
| case_status | VARCHAR | 51.2% | ACTIVE |  |
| detainer_prepared_criminality | VARCHAR | 0.0% | 2 Pending Criminal Charges |  |
| detention_facility | VARCHAR | 0.0% | QUEENS CENTRAL BOOKING |  |
| detention_facility_code | VARCHAR | 0.0% | QUEENNY | Facility identifier for detention location |
| facility_city | VARCHAR | 0.1% | QUEENS |  |
| detainer_prep_threat_level | DOUBLE | 5.6% | 1.0 |  |
| gender | VARCHAR | 0.0% | Female |  |
| citizenship_country | VARCHAR | 0.0% | COLOMBIA |  |
| birth_country | VARCHAR | 0.0% | COLOMBIA |  |
| birth_year | DOUBLE | 0.0% | 1991.0 |  |
| entry_status | VARCHAR | 23.6% | Not  Applicable |  |
| most_serious_conviction_msc_charge | VARCHAR | 71.5% | Homicide |  |
| msc_sentence_days | DOUBLE | 17.3% | 0.0 |  |
| msc_sentence_months | DOUBLE | 19.6% | 0.0 |  |
| msc_sentence_years | DOUBLE | 19.6% | 0.0 |  |
| msc_charge_code | VARCHAR | 71.5% | 0999 |  |
| msc_charge_date | TIMESTAMP | 71.5% | 2019-12-08 00:00:00 |  |
| msc_conviction_date | TIMESTAMP | 71.5% | 2023-08-16 00:00:00 |  |
| felon | VARCHAR | 0.1% | Not an Aggravated Felon |  |
| processing_disposition | VARCHAR | 0.0% | Detainer |  |
| case_category | VARCHAR | 51.2% | [8B] Excludable / Inadmissible - Under Adjudication by IJ |  |
| final_program | VARCHAR | 0.0% | ERO Criminal Alien Program |  |
| time_of_apprehension_case_category | VARCHAR | 86.1% | [8A] Excludable / Inadmissible - Hearing Not Commenced |  |
| time_of_apprehension_current_program | VARCHAR | 76.8% | ERO Criminal Alien Program |  |
| apprehension_method | VARCHAR | 76.7% | CAP Federal Incarceration |  |
| case_final_order_yes_no | VARCHAR | 51.2% | NO |  |
| final_order_date | TIMESTAMP | 70.9% | 2017-03-08 00:00:00 |  |
| apprehension_date | TIMESTAMP | 76.7% | 2023-11-09 11:06:00 | Arrest date, joins arrests to detentions by person+date |
| entry_date | TIMESTAMP | 87.0% | 2023-11-29 00:00:00 |  |
| prior_felony_yes_no | VARCHAR | 69.6% | NO |  |
| multiple_prior_misd_yes_no | VARCHAR | 76.4% | NO |  |
| violent_misdemeanor_yes_no | VARCHAR | 69.5% | NO |  |
| illegal_entry_yes_no | VARCHAR | 100.0% | NO |  |
| illegal_reentry_yes_no | VARCHAR | 96.6% | YES |  |
| immigration_fraud_yes_no | VARCHAR | 100.0% | NO |  |
| significant_risk_yes_no | VARCHAR | 77.7% | NO |  |
| other_removal_reason_yes_no | VARCHAR | 100.0% | NO |  |
| criminal_street_gang_yes_no | VARCHAR | 77.7% | NO |  |
| aggravated_felony_yes_no | VARCHAR | 74.9% | NO |  |
| deportation_ordered_yes_no | VARCHAR | 35.3% | YES |  |
| order_to_show_cause_served_yes_no | VARCHAR | 37.1% | YES |  |
| biometric_match_yes_no | VARCHAR | 28.5% | YES |  |
| statements_made_yes_no | VARCHAR | 33.0% | NO |  |
| unlawful_attempt_yes_no | VARCHAR | 100.0% | NO |  |
| unlawful_entry_yes_no | VARCHAR | 100.0% | YES |  |
| visa_yes_no | VARCHAR | 100.0% | NO |  |
| final_order_yes_no | VARCHAR | 51.2% | NO |  |
| federal_interest_yes_no | VARCHAR | 100.0% | NO |  |
| resume_custody_yes_no | VARCHAR | 0.0% | NO |  |
| detainer_lift_reason | VARCHAR | 37.4% | Detainer Declined by LEA |  |
| detainer_type | VARCHAR | 0.0% | I247A - Immigration Detainer - Notice of Action (as of May 2025) |  |
| alien_file_number | VARCHAR | 12.9% | (b)(6), (b)(7)(c) |  |
| case_id | VARCHAR | 51.2% | (b)(6), (b)(7)(c) (b)(7)(e) | EID case identifier |
| subject_id | VARCHAR | 0.0% | (b)(6), (b)(7)(c) (b)(7)(e) |  |
| eid_dta_id | VARCHAR | 0.0% | (b)(6), (b)(7)(c) (b)(7)(e) |  |
| unique_id | VARCHAR | 12.9% | 000038b86db2d5a0689a047fe3329f5f9f5336f0 | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2025 | Release identifier (release_2023 or release_2025) |

## detentions

Detention stays (book-in to book-out)

Rows: 8,944,408

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| detention_id | VARCHAR | 16.8% | (b)(6)(b)(7)(c) |  |
| case_id | VARCHAR | 1.0% | (b)(6)(b)(7)(c) | EID case identifier |
| subject_id | VARCHAR | 0.0% | (b)(6)(b)(7)(c) |  |
| stay_book_in_date | TIMESTAMP | 0.0% | 2012-11-25 00:00:00 | Detention start date |
| detention_book_in_date | TIMESTAMP | 0.0% | 2012-11-25 00:00:00 |  |
| detention_facility | VARCHAR | 0.0% | FLORENCE STAGING FACILITY |  |
| detention_facility_code | VARCHAR | 0.0% | FSF | Facility identifier for detention location |
| detention_book_out_date | TIMESTAMP | 1.1% | 2012-11-26 00:00:00 |  |
| detention_release_reason | VARCHAR | 1.1% | Transferred |  |
| stay_book_out_date | TIMESTAMP | 2.5% | 2012-11-30 00:00:00 |  |
| stay_release_reason | VARCHAR | 2.5% | Removed |  |
| religion | VARCHAR | 97.0% | NTA |  |
| marital | VARCHAR | 4.2% | Single |  |
| gender | VARCHAR | 0.0% | Male |  |
| ethnicity | VARCHAR | 56.5% | Hispanic Origin |  |
| alien_file_number | VARCHAR | 0.4% | (b)(6)(b)(7)(c) |  |
| birth_year | DOUBLE | 0.0% | 1979.0 |  |
| entry_status | VARCHAR | 4.0% | PWA Mexico |  |
| bond_posted_date | TIMESTAMP | 87.0% | 2011-08-02 00:00:00 |  |
| bond_posted_amount | DOUBLE | 87.0% | 7500.0 |  |
| initial_bond_set_amount | DOUBLE | 85.4% | 7500.0 |  |
| case_status | VARCHAR | 1.0% | 6-Deported/Removed - Deportability |  |
| case_category | VARCHAR | 1.0% | [16] Reinstated Final Order |  |
| final_order_yes_no | VARCHAR | 1.0% | YES |  |
| final_order_date | TIMESTAMP | 30.6% | 2012-11-24 00:00:00 |  |
| departed_date | TIMESTAMP | 33.5% | 2012-11-30 00:00:00 |  |
| departure_country | VARCHAR | 33.5% | GUATEMALA |  |
| case_threat_level | DOUBLE | 54.3% | 3.0 |  |
| charge | VARCHAR | 45.3% | PREVIOUSLY ORDERED REMOVED AND ENTERED OR ATTEMPTED TO ENTER WITHOUT BEING AD... |  |
| charge_code | VARCHAR | 45.3% | I9C2 |  |
| charge_section_code | VARCHAR | 45.3% | 212a9CiII |  |
| unique_id | VARCHAR | 0.4% | 00022a10812c798e9d38f70ae1b253500ce357cf | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023 or release_2025) |
| stay_book_out_date_time | TIMESTAMP | 85.0% | 2025-03-11 10:36:00 |  |
| felon | VARCHAR | 91.8% | Not an Aggravated Felon |  |
| book_in_criminality | VARCHAR | 83.2% | 1 Convicted Criminal |  |
| final_charge | VARCHAR | 88.4% | ALIEN PRESENT WITHOUT ADMISSION OR PAROLE - (PWAs) |  |
| citizenship_country | VARCHAR | 83.2% | HONDURAS |  |
| final_program | VARCHAR | 83.2% | ERO Criminal Alien Program |  |
| msc_charge_code | VARCHAR | 94.5% | 4199 |  |
| msc_charge | VARCHAR | 94.5% | Liquor |  |

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
| risk_of_flight | VARCHAR | 16.1% | Medium |  |
| special_vulnerability | VARCHAR | 17.9% | NONE |  |
| rca_case_number | VARCHAR | 68.6% | b(7)(e) |  |
| case_cat_at_rca_decision | VARCHAR | 68.6% | 5B |  |
| fo_at_rca_decision | VARCHAR | 0.0% | Y |  |
| fo_date_at_rca_decision | TIMESTAMP | 70.4% | 2012-02-27 00:00:00 |  |
| removal_likely_at_rca_decision | VARCHAR | 89.4% | Y |  |
| man_det_per_stat_alleg | VARCHAR | 31.4% | N |  |
| rca_decision_type | VARCHAR | 0.0% | Detain/Release  |  |
| rca_recommendation | VARCHAR | 0.0% | Supervisor to Determine - Detain or Release on Community Supervision |  |
| rca_bond_recommendation | DOUBLE | 93.6% | 4000.0 |  |
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
| fiscal_year_code | BIGINT | 0.0% | 2012 |  |
| fiscal_quarter_name | VARCHAR | 0.0% | Q4 |  |
| unique_id | VARCHAR | 0.3% | 00001ed059f30ad45f361ac3e86087cc9854a1fb | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023 or release_2025) |
| special_vulnerability_comments | VARCHAR | 99.6% | b(6), b(7)(c) |  |
| reason_removal_unlikely_at_rca_decision | VARCHAR | 99.4% | Other-DACS MIGRATED FINAL ORDER. VERIFY BEFORE REMOVAL |  |
| officer_comments | VARCHAR | 97.3% | b(6), b(7)(c) |  |
| supervisor_comments | VARCHAR | 96.7% | b(6), b(7)(c) |  |
| sujb_id | VARCHAR | 90.0% | (b)(6),(b)(7)(c) |  |

## removals

Deportation/removal records

Rows: 2,771,219

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| departure_date | TIMESTAMP | 0.0% | 2012-12-02 00:00:00 | Removal/departure date |
| port_of_departure | VARCHAR | 0.0% | DEL RIO, TX, POE |  |
| departure_country | VARCHAR | 0.0% | MEXICO |  |
| case_status | VARCHAR | 0.0% | 8-Excluded/Removed - Inadmissibility |  |
| case_category | VARCHAR | 0.0% | [8F] Expedited Removal |  |
| final_order_yes_no | VARCHAR | 0.0% | YES |  |
| final_order_date | TIMESTAMP | 5.8% | 2012-11-29 00:00:00 |  |
| case_id | VARCHAR | 0.0% | (b)(6),(b)(7)(c) | EID case identifier |
| gender | VARCHAR | 0.0% | Male |  |
| birth_country | VARCHAR | 0.0% | MEXICO |  |
| citizenship_country | VARCHAR | 0.0% | MEXICO |  |
| birth_year | DOUBLE | 0.0% | 1989.0 |  |
| alien_file_number | VARCHAR | 0.4% | (b)(6),(b)(7)(c) |  |
| entry_status | VARCHAR | 0.9% | PWA Mexico |  |
| entry_date | TIMESTAMP | 26.2% | 2012-11-28 00:00:00 |  |
| msc_charge | VARCHAR | 43.5% | Marijuana - Sell |  |
| msc_charge_date | TIMESTAMP | 46.1% | 2012-10-15 00:00:00 |  |
| msc_charge_code | VARCHAR | 43.5% | 3560 |  |
| msc_conviction_date | TIMESTAMP | 43.5% | 2013-03-25 00:00:00 |  |
| msc_criminal_charge_status | VARCHAR | 43.5% | Convicted |  |
| case_threat_level | DOUBLE | 43.5% | 1.0 |  |
| processing_disposition_code | VARCHAR | 0.1% | ER |  |
| processing_disposition | VARCHAR | 0.1% | Expedited Removal (I-860) |  |
| current_program | VARCHAR | 1.0% | Border Patrol |  |
| apprehension_date | TIMESTAMP | 1.4% | 2012-11-28 12:00:00 | Arrest date, joins arrests to detentions by person+date |
| charge_section_code | VARCHAR | 0.4% | 212a7AiI |  |
| charge_code | VARCHAR | 0.4% | I7A1 |  |
| unique_id | VARCHAR | 0.4% | 00005110ce5ae46e9f1bbb35aca8a19d9799b851 | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023 or release_2025) |

## v_arrest_to_detention

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| apprehension_date | TIMESTAMP | 0.0% | 2018-05-31 00:00:00 | Arrest date, joins arrests to detentions by person+date |
| apprehension_method | VARCHAR | 0.0% | Located |  |
| arrest_created_by | VARCHAR | 14.8% | (b)(6)(b)(7)(c) |  |
| case_id | VARCHAR | 2.1% | (b)(6)(b)(7)(c) | EID case identifier |
| subject_id | VARCHAR | 0.0% | (b)(6), (b)(7)(c) (b)(7)(e) |  |
| alien_file_number | VARCHAR | 0.3% | (b)(6)(b)(7)(c) |  |
| unique_id | VARCHAR | 0.3% | 00031dd2aaab192a3cee3721ce6eba7760a34046 | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2025 | Release identifier (release_2023 or release_2025) |
| apprehension_state | VARCHAR | 87.4% | TEXAS |  |
| apprehension_aor | VARCHAR | 85.4% | Atlanta Area of Responsibility |  |
| final_program | VARCHAR | 85.2% | ERO Criminal Alien Program |  |
| final_program_group | VARCHAR | 85.2% | ICE |  |
| apprehension_criminality | VARCHAR | 85.2% | 2 Pending Criminal Charges |  |
| case_status | VARCHAR | 85.4% | ACTIVE |  |
| case_category | VARCHAR | 85.4% | [8C] Excludable / Inadmissible - Administrative Final Order Issued |  |
| departed_date | TIMESTAMP | 89.5% | 2024-02-08 00:00:00 |  |
| departure_country | VARCHAR | 89.5% | BRAZIL |  |
| final_order_yes_no | VARCHAR | 85.4% | YES |  |
| final_order_date | TIMESTAMP | 89.7% | 2024-01-04 00:00:00 |  |
| birth_year | DOUBLE | 85.2% | 1989.0 |  |
| citizenship_country | VARCHAR | 85.2% | GUATEMALA |  |
| gender | VARCHAR | 85.2% | Male |  |
| apprehension_site_landmark | VARCHAR | 85.4% | PULASKI COUNTY JAIL |  |
| stay_book_in_date | TIMESTAMP | 5.0% | 2024-10-30 12:38:00 | Detention start date |
| stay_book_out_date | TIMESTAMP | 7.2% | 2012-11-09 00:00:00 |  |
| detention_release_reason | VARCHAR | 5.8% | Removed |  |
| detention_facility | VARCHAR | 5.0% | OTAY MESA DETENTION CENTER |  |
| days_arrest_to_detention | BIGINT | 5.0% | 0 |  |
| days_in_detention | BIGINT | 7.2% | 31 |  |

## v_daily_arrests

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| date | DATE | 0.0% | 2011-10-01 |  |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023 or release_2025) |
| arrest_count | BIGINT | 0.0% | 142 |  |

## v_enforcement_pipeline

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unique_id | VARCHAR | 0.2% | 0003e37ef6e337b44a9604d9dbe7d52b255ed2ea | Anonymized person ID, links across arrests, detainers, detentions, removals |
| apprehension_date | TIMESTAMP | 0.0% | 2012-07-19 00:00:00 | Arrest date, joins arrests to detentions by person+date |
| arrest_source | VARCHAR | 0.0% | release_2023 |  |
| stay_book_in_date | TIMESTAMP | 2.7% | 2013-04-02 00:00:00 | Detention start date |
| stay_book_out_date | TIMESTAMP | 4.0% | 2013-04-02 00:00:00 |  |
| detention_facility | VARCHAR | 2.7% | BIG SPRING HOLD ROOM |  |
| departure_date | TIMESTAMP | 16.6% | 2012-11-01 00:00:00 | Removal/departure date |
| removal_country | VARCHAR | 16.6% | MEXICO |  |
| days_to_detention | BIGINT | 2.7% | 202 |  |
| days_detained | BIGINT | 4.0% | 0 |  |
| days_to_removal | BIGINT | 16.6% | -1911 |  |
