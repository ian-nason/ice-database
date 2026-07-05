# Data Dictionary

Source: [Deportation Data Project](https://deportationdata.org)

## arrests

ICE administrative arrests

Rows: 2,334,315

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| apprehension_date | TIMESTAMP | 0.0% | 2015-10-26 00:00:00 | Arrest date, joins arrests to detentions by person+date |
| apprehension_method | VARCHAR | 0.0% | Non-Custodial Arrest |  |
| arrest_created_by | VARCHAR | 30.4% | (b)(6)(b)(7)(c) |  |
| case_id | VARCHAR | 32.5% | (b)(6)(b)(7)(c) | EID case identifier |
| subject_id | VARCHAR | 30.4% | (b)(6)(b)(7)(c) |  |
| alien_file_number | VARCHAR | 31.1% | (b)(6)(b)(7)(c) |  |
| unique_id | VARCHAR | 1.3% | f62520f6cfab8ad227a064a1e9e633d15c7ca3b7 | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023, release_2025, or release_2026) |
| apprehension_state | VARCHAR | 100.0% |  |  |
| apprehension_aor | VARCHAR | 100.0% |  |  |
| final_program | VARCHAR | 100.0% |  |  |
| final_program_group | VARCHAR | 100.0% |  |  |
| apprehension_criminality | VARCHAR | 69.6% | 3 Other Immigration Violator |  |
| case_status | VARCHAR | 70.4% | A-Proceedings Terminated |  |
| case_category | VARCHAR | 70.4% | [8B] Excludable / Inadmissible - Under Adjudication by IJ |  |
| departed_date | TIMESTAMP | 81.3% | 2023-11-17 00:00:00 |  |
| departure_country | VARCHAR | 81.3% | MEXICO |  |
| final_order_yes_no | VARCHAR | 70.4% | NO |  |
| final_order_date | TIMESTAMP | 83.4% | 2023-09-27 00:00:00 |  |
| birth_year | DOUBLE | 69.6% | 2020.0 |  |
| citizenship_country | VARCHAR | 69.6% | CUBA |  |
| gender | VARCHAR | 69.6% | Female |  |
| apprehension_site_landmark | VARCHAR | 70.2% | PCB GENERAL AREA, NON-SPECIFIC |  |
| apprehension_type | VARCHAR | 89.5% | Targeted |  |
| state | VARCHAR | 74.1% | MINNESOTA |  |
| toa_current_duty_aor | VARCHAR | 69.9% | St. Paul Area of Responsibility |  |
| apprehension_final_program | VARCHAR | 69.6% | Non-Detained Docket Control |  |
| arresting_agency | VARCHAR | 69.6% | ICE |  |
| operation | VARCHAR | 92.4% | - |  |
| toa_current_duty_site | VARCHAR | 69.6% | PITTSBURGH, PA, DOCKET CONTROL OFFICE |  |
| case_criminality | VARCHAR | 70.4% | 2 Pending Criminal Charges |  |
| case_threat_level | DOUBLE | 88.9% | 1.0 |  |

## detainers

Detainer requests issued to jails/prisons

Rows: 597,009

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| detainer_prepare_date | TIMESTAMP | 0.0% | 2024-12-08 00:00:00 |  |
| facility_state | VARCHAR | 0.1% | FLORIDA |  |
| facility_aor | VARCHAR | 19.9% | Newark Area of Responsibility |  |
| port_of_departure | VARCHAR | 69.4% | LAREDO, TX, POE |  |
| departure_country | VARCHAR | 69.4% | MEXICO |  |
| departed_date | TIMESTAMP | 69.3% | 2023-12-26 00:00:00 |  |
| case_status | VARCHAR | 49.3% | ACTIVE |  |
| detainer_prepared_criminality | VARCHAR | 100.0% |  |  |
| detention_facility | VARCHAR | 100.0% |  |  |
| detention_facility_code | VARCHAR | 100.0% |  | Facility identifier for detention location |
| facility_city | VARCHAR | 0.1% | ORLANDO |  |
| detainer_prep_threat_level | DOUBLE | 100.0% |  |  |
| gender | VARCHAR | 0.0% | Male |  |
| citizenship_country | VARCHAR | 0.0% | HONDURAS |  |
| birth_country | VARCHAR | 0.0% | MEXICO |  |
| birth_year | DOUBLE | 0.0% | 1985.0 |  |
| entry_status | VARCHAR | 23.6% | Not  Applicable |  |
| most_serious_conviction_msc_charge | VARCHAR | 100.0% |  |  |
| msc_sentence_days | DOUBLE | 91.0% | 490.0 |  |
| msc_sentence_months | DOUBLE | 93.4% | 12.0 |  |
| msc_sentence_years | DOUBLE | 93.2% | 20.0 |  |
| msc_charge_code | VARCHAR | 72.1% | 1315 |  |
| msc_charge_date | TIMESTAMP | 72.1% | 2024-05-20 00:00:00 |  |
| msc_conviction_date | TIMESTAMP | 72.1% | 2016-12-09 00:00:00 |  |
| felon | VARCHAR | 100.0% |  |  |
| processing_disposition | VARCHAR | 0.0% | Detainer |  |
| case_category | VARCHAR | 49.3% | [8A] Excludable / Inadmissible - Hearing Not Commenced |  |
| final_program | VARCHAR | 100.0% |  |  |
| time_of_apprehension_case_category | VARCHAR | 100.0% |  |  |
| time_of_apprehension_current_program | VARCHAR | 100.0% |  |  |
| apprehension_method | VARCHAR | 75.0% | CAP Local Incarceration |  |
| case_final_order_yes_no | VARCHAR | 100.0% |  |  |
| final_order_date | TIMESTAMP | 68.5% | 2024-08-07 00:00:00 |  |
| apprehension_date | TIMESTAMP | 75.0% | 2023-08-24 07:30:00 | Arrest date, joins arrests to detentions by person+date |
| entry_date | TIMESTAMP | 86.7% | 2022-08-17 00:00:00 |  |
| prior_felony_yes_no | VARCHAR | 63.6% | YES |  |
| multiple_prior_misd_yes_no | VARCHAR | 70.5% | YES |  |
| violent_misdemeanor_yes_no | VARCHAR | 63.5% | YES |  |
| illegal_entry_yes_no | VARCHAR | 100.0% | NO |  |
| illegal_reentry_yes_no | VARCHAR | 71.9% | NO |  |
| immigration_fraud_yes_no | VARCHAR | 100.0% | NO |  |
| significant_risk_yes_no | VARCHAR | 71.9% | NO |  |
| other_removal_reason_yes_no | VARCHAR | 100.0% | NO |  |
| criminal_street_gang_yes_no | VARCHAR | 71.9% | NO |  |
| aggravated_felony_yes_no | VARCHAR | 68.9% | YES |  |
| deportation_ordered_yes_no | VARCHAR | 19.6% | NO |  |
| order_to_show_cause_served_yes_no | VARCHAR | 19.6% | NO |  |
| biometric_match_yes_no | VARCHAR | 19.6% | YES |  |
| statements_made_yes_no | VARCHAR | 19.6% | NO |  |
| unlawful_attempt_yes_no | VARCHAR | 100.0% | NO |  |
| unlawful_entry_yes_no | VARCHAR | 100.0% | NO |  |
| visa_yes_no | VARCHAR | 100.0% | NO |  |
| final_order_yes_no | VARCHAR | 49.3% | YES |  |
| federal_interest_yes_no | VARCHAR | 100.0% |  |  |
| resume_custody_yes_no | VARCHAR | 0.0% | NO |  |
| detainer_lift_reason | VARCHAR | 33.4% | Booked into Detention |  |
| detainer_type | VARCHAR | 0.0% | I247A - Immigration Detainer - Immigration Detainer - Notice of Action |  |
| alien_file_number | VARCHAR | 100.0% |  |  |
| case_id | VARCHAR | 100.0% |  | EID case identifier |
| subject_id | VARCHAR | 100.0% |  |  |
| eid_dta_id | VARCHAR | 0.0% | b(6), b(7)c |  |
| unique_id | VARCHAR | 12.5% | b13b15dd9e7564ab2e881f43148268a3b867f70d | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2026 | Release identifier (release_2023, release_2025, or release_2026) |
| detainer_criminality | VARCHAR | 0.0% | 2 Pending Criminal Charges |  |
| detainer_facility | VARCHAR | 0.0% | WEST VALLEY DETENTION CENTER |  |
| detainer_facility_code | VARCHAR | 0.0% | SFCOJCA |  |
| detainer_threat_level | DOUBLE | 6.8% | 1.0 |  |
| msc_charge | VARCHAR | 72.1% | Sex Assault |  |
| aggravated_felon_yes_no | VARCHAR | 0.1% | Not an Aggravated Felon |  |
| toa_case_category | VARCHAR | 85.7% | [16] Reinstated Final Order |  |
| toa_current_program | VARCHAR | 75.1% | ERO Criminal Alien Program |  |
| federal_register_notice_yes_no | VARCHAR | 42.6% | YES |  |
| detainer_lift_reason_code | VARCHAR | 33.4% | B |  |
| active_investigation_yes_no | VARCHAR | 100.0% | YES |  |
| notify_release_request_yes_no | VARCHAR | 100.0% | NO |  |
| tod_current_duty_site | VARCHAR | 0.1% | ERO - Pacific Enforcement Response Center |  |

## detentions

Detention stays (book-in to book-out)

Rows: 9,306,513

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| detention_id | VARCHAR | 26.0% | (b)(6)(b)(7)(c) |  |
| case_id | VARCHAR | 26.9% | (b)(6)(b)(7)(c) | EID case identifier |
| subject_id | VARCHAR | 26.0% | (b)(6)(b)(7)(c) |  |
| stay_book_in_date | TIMESTAMP | 0.0% | 2012-04-07 00:00:00 | Detention start date |
| detention_book_in_date | TIMESTAMP | 0.0% | 2012-04-07 00:00:00 |  |
| detention_facility | VARCHAR | 0.0% | FLORENCE STAGING FACILITY |  |
| detention_facility_code | VARCHAR | 0.0% | FSF | Facility identifier for detention location |
| detention_book_out_date | TIMESTAMP | 26.0% | 2012-04-08 00:00:00 |  |
| detention_release_reason | VARCHAR | 0.6% | Removed |  |
| stay_book_out_date | TIMESTAMP | 1.7% | 2014-08-13 00:00:00 |  |
| stay_release_reason | VARCHAR | 1.7% | Removed |  |
| religion | VARCHAR | 97.1% | NTA |  |
| marital | VARCHAR | 0.7% | Married |  |
| gender | VARCHAR | 0.0% | Male |  |
| ethnicity | VARCHAR | 54.9% | Hispanic Origin |  |
| alien_file_number | VARCHAR | 26.4% | (b)(6)(b)(7)(c) |  |
| birth_year | DOUBLE | 0.0% | 1986.0 |  |
| entry_status | VARCHAR | 4.7% | PWA Mexico |  |
| bond_posted_date | TIMESTAMP | 87.1% | 2012-05-03 00:00:00 |  |
| bond_posted_amount | DOUBLE | 87.1% | 1500.0 |  |
| initial_bond_set_amount | DOUBLE | 85.7% | 7500.0 |  |
| case_status | VARCHAR | 1.0% | 8-Excluded/Removed - Inadmissibility |  |
| case_category | VARCHAR | 1.0% | [16] Reinstated Final Order |  |
| final_order_yes_no | VARCHAR | 1.0% | YES |  |
| final_order_date | TIMESTAMP | 30.6% | 2012-11-29 00:00:00 |  |
| departed_date | TIMESTAMP | 31.5% | 2012-12-21 00:00:00 |  |
| departure_country | VARCHAR | 31.6% | GUATEMALA |  |
| case_threat_level | DOUBLE | 54.9% | 2.0 |  |
| charge | VARCHAR | 50.2% | IMMIGRANT WITHOUT AN IMMIGRANT VISA |  |
| charge_code | VARCHAR | 50.2% | I7A1 |  |
| charge_section_code | VARCHAR | 50.2% | 212a7AiI |  |
| unique_id | VARCHAR | 0.4% | eab5153b48965fceac6f5ca727a34ae4a2676e2e | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023, release_2025, or release_2026) |
| stay_book_out_date_time | TIMESTAMP | 75.7% | 2023-07-12 09:38:00 |  |
| felon | VARCHAR | 100.0% |  |  |
| book_in_criminality | VARCHAR | 74.0% | 1 Convicted Criminal |  |
| final_charge | VARCHAR | 81.5% | NONIMMIGRANT OVERSTAY |  |
| citizenship_country | VARCHAR | 74.0% | VENEZUELA |  |
| final_program | VARCHAR | 100.0% |  |  |
| msc_charge_code | VARCHAR | 91.7% | 1399 |  |
| msc_charge | VARCHAR | 91.7% | Trespassing |  |
| book_out_date_time | TIMESTAMP | 74.6% | 2023-07-12 09:38:00 |  |
| birth_country | VARCHAR | 74.0% | SENEGAL |  |
| known_terrorist_yes_no | VARCHAR | 74.0% | NO |  |
| suspected_gang_yes_no | VARCHAR | 74.0% | NO |  |
| msc_sentence_days | DOUBLE | 97.2% | 12.0 |  |
| msc_sentence_months | DOUBLE | 98.3% | 97.0 |  |
| msc_sentence_years | DOUBLE | 98.5% | 2.0 |  |
| aggravated_felon_yes_no | VARCHAR | 87.1% | Not an Aggravated Felon |  |
| offense_ina_236c_yes_no | VARCHAR | 74.8% | N |  |
| case_ina_236c_yes_no | VARCHAR | 74.1% | N |  |
| detainee_classification | VARCHAR | 74.0% | Low |  |
| initial_bond_set_date | TIMESTAMP | 99.8% | 2019-09-05 00:00:00 |  |
| race | VARCHAR | 74.4% | White |  |
| entry_date | TIMESTAMP | 84.3% | 2023-03-21 00:00:00 |  |
| apprehension_final_program | VARCHAR | 74.8% | Border Patrol |  |
| msc_charge_date | TIMESTAMP | 91.9% | 2023-07-08 00:00:00 |  |
| msc_conviction_date | TIMESTAMP | 91.7% | 2022-11-02 00:00:00 |  |
| msc_criminal_charge_status | VARCHAR | 91.7% | Convicted |  |
| msc_criminal_charge_status_code | VARCHAR | 91.7% | C |  |
| msc_crime_class | VARCHAR | 92.0% | Felony |  |
| book_in_site | VARCHAR | 74.0% | HARLINGEN, TX, DOCKET CONTROL OFFICE |  |
| book_in_aor | VARCHAR | 74.0% | New Orleans Area of Responsibility |  |

## encounters

ICE encounters with individuals

Rows: 2,598,612

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| event_date | TIMESTAMP | 0.0% | 2025-06-26 00:00:00 |  |
| event_type | VARCHAR | 0.0% | CAP Local |  |
| event_landmark | VARCHAR | 55.6% | AUS GENERAL AREA, NON-SPECIFIC |  |
| operation | VARCHAR | 89.2% | - |  |
| encounter_threat_level | VARCHAR | 67.7% | 3 |  |
| responsible_aor | VARCHAR | 3.0% | Boston Area of Responsibility |  |
| responsible_site | VARCHAR | 0.0% | BOSTON, MA, DOCKET CONTROL OFFICE |  |
| lead_event_type | VARCHAR | 0.0% | CAP Local |  |
| lead_source | VARCHAR | 84.4% | Other Lead |  |
| final_program | VARCHAR | 0.0% | ERO Criminal Alien Program |  |
| arresting_agency | VARCHAR | 0.0% | ICE |  |
| encounter_criminality | VARCHAR | 0.0% | 3 Other Immigration Violator |  |
| processing_disposition | VARCHAR | 0.1% | Other |  |
| case_status | VARCHAR | 51.7% | 6-Deported/Removed - Deportability |  |
| case_category | VARCHAR | 51.7% | [8B] Excludable / Inadmissible - Under Adjudication by IJ |  |
| departed_date | TIMESTAMP | 78.1% | 2024-04-09 00:00:00 |  |
| departure_country | VARCHAR | 78.1% | MEXICO |  |
| final_order_yes_no | VARCHAR | 51.7% | YES |  |
| final_order_date | TIMESTAMP | 77.9% | 2001-02-08 00:00:00 |  |
| birth_year | DOUBLE | 0.2% | 1989.0 |  |
| citizenship_county | VARCHAR | 0.0% | UNKNOWN |  |
| gender | VARCHAR | 0.0% | Male |  |
| unique_id | VARCHAR | 10.8% | 4019f115eed35c4f238bfdeb4648978399575e15 | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2026 | Release identifier (release_2023, release_2025, or release_2026) |

## rca_decisions

Release/custody assessment decision history

Rows: 3,543,467

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| rca_aor | VARCHAR | 0.0% | SLC |  |
| rca_dco | VARCHAR | 0.0% | PIC |  |
| a_number | VARCHAR | 0.3% | b(6), b(7)(c) |  |
| subj_id | VARCHAR | 10.0% | b(6), b(7)(c) |  |
| last_name | VARCHAR | 0.0% | b(6), b(7)(c) |  |
| first_name | VARCHAR | 0.0% | b(6), b(7)(c) |  |
| alert_code | VARCHAR | 56.5% | 2, M |  |
| active_inactive | VARCHAR | 0.0% | Active |  |
| submission_date | TIMESTAMP | 16.1% | 2017-01-08 00:00:00 |  |
| status_code | VARCHAR | 26.1% | C |  |
| risk_to_public_safety | VARCHAR | 16.1% | Low |  |
| risk_of_flight | VARCHAR | 16.1% | Medium |  |
| special_vulnerability | VARCHAR | 17.9% | NONE |  |
| rca_case_number | VARCHAR | 68.6% | b(7)(e) |  |
| case_cat_at_rca_decision | VARCHAR | 68.6% | 5B |  |
| fo_at_rca_decision | VARCHAR | 0.0% | Y |  |
| fo_date_at_rca_decision | TIMESTAMP | 70.4% | 2014-03-27 00:00:00 |  |
| removal_likely_at_rca_decision | VARCHAR | 89.4% | Y |  |
| man_det_per_stat_alleg | VARCHAR | 31.4% | N |  |
| rca_decision_type | VARCHAR | 0.0% | Detain/Release  |  |
| rca_recommendation | VARCHAR | 0.0% | Supervisor to Determine - Detain or Release on Community Supervision |  |
| rca_bond_recommendation | DOUBLE | 93.6% | 7000.0 |  |
| officer_id | VARCHAR | 16.1% | b(6), b(7)(c)   |  |
| officer_agree_disagree | VARCHAR | 16.1% | Not Applicable, Supervisor to Determine |  |
| supervisor_id | VARCHAR | 1.8% | b(6), b(7)(c) |  |
| supervisor_agree_disagree | VARCHAR | 0.0% | Not Applicable, Supervisor to Determine |  |
| rca_final_decision | VARCHAR | 0.0% | Detain in the Custody of This Service |  |
| final_bond_amount | DOUBLE | 98.0% | 10000.0 |  |
| rca_decision_date | TIMESTAMP | 0.0% | 2017-01-08 00:00:00 |  |
| rca_scoring_ver | DOUBLE | 16.1% | 1.2 |  |
| spec_vuln_ver | DOUBLE | 16.1% | 1.0 |  |
| man_det_ver | DOUBLE | 91.9% | 1.0 |  |
| disc_infr_ver | DOUBLE | 99.8% | 1.0 |  |
| fiscal_year_code | BIGINT | 0.0% | 2012 |  |
| fiscal_quarter_name | VARCHAR | 0.0% | Q4 |  |
| unique_id | VARCHAR | 0.3% | 00001ed059f30ad45f361ac3e86087cc9854a1fb | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023, release_2025, or release_2026) |
| special_vulnerability_comments | VARCHAR | 99.6% | b(6), b(7)(c) |  |
| reason_removal_unlikely_at_rca_decision | VARCHAR | 99.4% | Not in ICE Custody |  |
| officer_comments | VARCHAR | 97.3% | b(6), b(7)(c) |  |
| supervisor_comments | VARCHAR | 96.7% | b(6), b(7)(c) |  |
| sujb_id | VARCHAR | 90.0% | (b)(6),(b)(7)(c) |  |

## removals

Deportation/removal records

Rows: 3,680,770

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| departure_date | TIMESTAMP | 0.0% | 2013-04-09 00:00:00 | Removal/departure date |
| port_of_departure | VARCHAR | 0.0% | NEWARK INTERNATIONAL AIRPORT, NEWARK NJ, POE |  |
| departure_country | VARCHAR | 0.0% | MEXICO |  |
| case_status | VARCHAR | 0.0% | 6-Deported/Removed - Deportability |  |
| case_category | VARCHAR | 0.0% | [16] Reinstated Final Order |  |
| final_order_yes_no | VARCHAR | 0.0% | YES |  |
| final_order_date | TIMESTAMP | 9.7% | 2006-10-06 00:00:00 |  |
| case_id | VARCHAR | 28.6% | (b)(6),(b)(7)(c) | EID case identifier |
| gender | VARCHAR | 0.0% | Male |  |
| birth_country | VARCHAR | 0.0% | MEXICO |  |
| citizenship_country | VARCHAR | 0.0% | MEXICO |  |
| birth_year | DOUBLE | 0.0% | 1969.0 |  |
| alien_file_number | VARCHAR | 28.9% | (b)(6),(b)(7)(c) |  |
| entry_status | VARCHAR | 1.6% | PWA Mexico |  |
| entry_date | TIMESTAMP | 25.0% | 2006-09-11 00:00:00 |  |
| msc_charge | VARCHAR | 51.3% | Illegal Re-Entry (INA SEC.101(a)(43)(O), 8USC1326 only) |  |
| msc_charge_date | TIMESTAMP | 53.5% | 2001-10-20 00:00:00 |  |
| msc_charge_code | VARCHAR | 51.3% | 0999 |  |
| msc_conviction_date | TIMESTAMP | 51.3% | 2007-04-02 00:00:00 |  |
| msc_criminal_charge_status | VARCHAR | 51.3% | Convicted |  |
| case_threat_level | DOUBLE | 51.3% | 1.0 |  |
| processing_disposition_code | VARCHAR | 28.7% | REINST |  |
| processing_disposition | VARCHAR | 0.0% | REINSTATEMENT OF DEPORT ORDER I-871 |  |
| current_program | VARCHAR | 29.4% | Border Patrol |  |
| apprehension_date | TIMESTAMP | 29.5% | 2007-07-20 00:00:00 | Arrest date, joins arrests to detentions by person+date |
| charge_section_code | VARCHAR | 28.9% | 212a9Aii |  |
| charge_code | VARCHAR | 28.9% | I9A2 |  |
| unique_id | VARCHAR | 0.5% | d7e01d84275800c05eff1b0752fa989889096231 | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023, release_2025, or release_2026) |
| case_aor | VARCHAR | 71.4% | Dallas Area of Responsibility |  |
| state | VARCHAR | 93.6% | TENNESSEE |  |
| county | VARCHAR | 100.0% | KERN |  |
| known_terrorist_yes_no | VARCHAR | 71.4% | NO |  |
| suspected_gang_yes_no | VARCHAR | 71.4% | NO |  |
| case_criminality | VARCHAR | 71.4% | 1 Convicted Criminal |  |
| aggravated_felon_yes_no | VARCHAR | 88.1% | Not an Aggravated Felon |  |
| final_program | VARCHAR | 71.4% | Border Patrol |  |
| final_program_code | VARCHAR | 71.4% | BP |  |
| arresting_agency | VARCHAR | 71.4% | CBP |  |
| toa_case_category | VARCHAR | 95.5% | [16] Reinstated Final Order |  |
| latest_apprehension_final_program | VARCHAR | 71.6% | Border Patrol |  |
| latest_arresting_agency | VARCHAR | 71.6% | ICE |  |
| latest_apprehension_date | TIMESTAMP | 71.6% | 2022-12-02 10:34:00 |  |
| final_charge_code | VARCHAR | 71.4% | I7A1 |  |
| final_charge_section | VARCHAR | 71.4% | 212a9Aii |  |
| prior_deport_yes_no | VARCHAR | 71.4% | NO |  |

## v_arrest_to_detention

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| apprehension_date | TIMESTAMP | 0.0% | 2014-01-30 00:00:00 | Arrest date, joins arrests to detentions by person+date |
| apprehension_method | VARCHAR | 0.0% | Other Agency (turned over to INS) |  |
| arrest_created_by | VARCHAR | 25.8% | (b)(6)(b)(7)(c) |  |
| case_id | VARCHAR | 27.4% | (b)(6)(b)(7)(c) | EID case identifier |
| subject_id | VARCHAR | 25.8% | (b)(6)(b)(7)(c) |  |
| alien_file_number | VARCHAR | 26.0% | (b)(6)(b)(7)(c) |  |
| unique_id | VARCHAR | 0.4% | 477fda95c0cd1f9833656cdcd983d72ba76df4bf | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023, release_2025, or release_2026) |
| apprehension_state | VARCHAR | 100.0% |  |  |
| apprehension_aor | VARCHAR | 100.0% |  |  |
| final_program | VARCHAR | 100.0% |  |  |
| final_program_group | VARCHAR | 100.0% |  |  |
| apprehension_criminality | VARCHAR | 74.2% | 1 Convicted Criminal |  |
| case_status | VARCHAR | 74.6% | 8-Excluded/Removed - Inadmissibility |  |
| case_category | VARCHAR | 74.6% | [8C] Excludable / Inadmissible - Administrative Final Order Issued |  |
| departed_date | TIMESTAMP | 81.1% | 2022-12-19 00:00:00 |  |
| departure_country | VARCHAR | 81.1% | MEXICO |  |
| final_order_yes_no | VARCHAR | 74.6% | YES |  |
| final_order_date | TIMESTAMP | 83.2% | 2012-08-28 00:00:00 |  |
| birth_year | DOUBLE | 74.2% | 1983.0 |  |
| citizenship_country | VARCHAR | 74.2% | MEXICO |  |
| gender | VARCHAR | 74.2% | Male |  |
| apprehension_site_landmark | VARCHAR | 74.5% | CHILDRESS COUNTY |  |
| apprehension_type | VARCHAR | 90.4% | Collateral |  |
| state | VARCHAR | 77.5% | TEXAS |  |
| toa_current_duty_aor | VARCHAR | 74.4% | Dallas Area of Responsibility |  |
| apprehension_final_program | VARCHAR | 74.2% | ERO Criminal Alien Program |  |
| arresting_agency | VARCHAR | 74.2% | ICE |  |
| operation | VARCHAR | 94.9% | - |  |
| toa_current_duty_site | VARCHAR | 74.2% | ERO - Amarillo, TX Sub-Office |  |
| case_criminality | VARCHAR | 74.6% | 1 Convicted Criminal |  |
| case_threat_level | DOUBLE | 88.8% | 1.0 |  |
| stay_book_in_date | TIMESTAMP | 4.9% | 2012-10-12 00:00:00 | Detention start date |
| stay_book_out_date | TIMESTAMP | 7.0% | 2012-02-16 00:00:00 |  |
| detention_release_reason | VARCHAR | 5.7% | Removed |  |
| detention_facility | VARCHAR | 4.9% | PORTLAND DISTRICT OFFICE |  |
| days_arrest_to_detention | BIGINT | 4.9% | -574 |  |
| days_in_detention | BIGINT | 7.0% | 3 |  |

## v_daily_arrests

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| date | DATE | 0.0% | 2011-10-01 |  |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023, release_2025, or release_2026) |
| arrest_count | BIGINT | 0.0% | 142 |  |

## v_enforcement_pipeline

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unique_id | VARCHAR | 0.2% | 477fda95c0cd1f9833656cdcd983d72ba76df4bf | Anonymized person ID, links across arrests, detainers, detentions, removals |
| apprehension_date | TIMESTAMP | 0.0% | 2012-05-23 00:00:00 | Arrest date, joins arrests to detentions by person+date |
| arrest_source | VARCHAR | 0.0% | release_2023 |  |
| stay_book_in_date | TIMESTAMP | 2.9% | 2013-04-02 00:00:00 | Detention start date |
| stay_book_out_date | TIMESTAMP | 4.1% | 2013-06-11 00:00:00 |  |
| detention_facility | VARCHAR | 2.9% | YORK COUNTY JAIL, PA |  |
| departure_date | TIMESTAMP | 11.2% | 2012-10-18 00:00:00 | Removal/departure date |
| removal_country | VARCHAR | 11.2% | GUATEMALA |  |
| days_to_detention | BIGINT | 2.9% | 467 |  |
| days_detained | BIGINT | 4.1% | 0 |  |
| days_to_removal | BIGINT | 11.2% | -2472 |  |
