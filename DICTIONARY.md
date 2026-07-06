# Data Dictionary

Source: [Deportation Data Project](https://deportationdata.org)

## arrests

ICE administrative arrests

Rows: 2,334,315

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| apprehension_date | TIMESTAMP | 0.0% | 2015-10-26 00:00:00 | Arrest date, joins arrests to detentions by person+date |
| apprehension_method | VARCHAR | 0.0% | Located |  |
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
| departed_date | TIMESTAMP | 81.3% | 2026-01-21 00:00:00 |  |
| departure_country | VARCHAR | 81.3% | EL SALVADOR |  |
| final_order_yes_no | VARCHAR | 70.4% | YES |  |
| final_order_date | TIMESTAMP | 83.4% | 2025-11-21 00:00:00 |  |
| birth_year | DOUBLE | 69.6% | 1999.0 |  |
| citizenship_country | VARCHAR | 69.6% | GUATEMALA |  |
| gender | VARCHAR | 69.6% | Male |  |
| apprehension_site_landmark | VARCHAR | 70.2% | SLC GENERAL AREA, NON-SPECIFIC |  |
| apprehension_type | VARCHAR | 89.5% | Targeted |  |
| state | VARCHAR | 74.1% | COLORADO |  |
| toa_current_duty_aor | VARCHAR | 69.9% | Salt Lake City Area of Responsibility |  |
| apprehension_final_program | VARCHAR | 69.6% | ERO Criminal Alien Program |  |
| arresting_agency | VARCHAR | 69.6% | ICE |  |
| operation | VARCHAR | 92.4% | ICE Wall FY26 |  |
| toa_current_duty_site | VARCHAR | 69.6% | ERO - Tallahassee, FL Sub Office |  |
| case_criminality | VARCHAR | 70.4% | 3 Other Immigration Violator |  |
| case_threat_level | DOUBLE | 88.9% | 3.0 |  |

## detainers

Detainer requests issued to jails/prisons

Rows: 597,009

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| detainer_prepare_date | TIMESTAMP | 0.0% | 2024-03-07 00:00:00 |  |
| facility_state | VARCHAR | 0.1% | TEXAS |  |
| facility_aor | VARCHAR | 19.9% | Miami Area of Responsibility |  |
| port_of_departure | VARCHAR | 69.4% | LAREDO, TX, POE |  |
| departure_country | VARCHAR | 69.4% | HONDURAS |  |
| departed_date | TIMESTAMP | 69.3% | 2025-09-10 00:00:00 |  |
| case_status | VARCHAR | 49.3% | 8-Excluded/Removed - Inadmissibility |  |
| detainer_prepared_criminality | VARCHAR | 100.0% |  |  |
| detention_facility | VARCHAR | 100.0% |  |  |
| detention_facility_code | VARCHAR | 100.0% |  | Facility identifier for detention location |
| facility_city | VARCHAR | 0.1% | GARDENA |  |
| detainer_prep_threat_level | DOUBLE | 100.0% |  |  |
| gender | VARCHAR | 0.0% | Male |  |
| citizenship_country | VARCHAR | 0.0% | CUBA |  |
| birth_country | VARCHAR | 0.0% | MEXICO |  |
| birth_year | DOUBLE | 0.0% | 1989.0 |  |
| entry_status | VARCHAR | 23.6% | Not  Applicable |  |
| most_serious_conviction_msc_charge | VARCHAR | 100.0% |  |  |
| msc_sentence_days | DOUBLE | 91.0% | 1.0 |  |
| msc_sentence_months | DOUBLE | 93.4% | 10.0 |  |
| msc_sentence_years | DOUBLE | 93.2% | 20.0 |  |
| msc_charge_code | VARCHAR | 72.1% | 6410 |  |
| msc_charge_date | TIMESTAMP | 72.1% | 2020-02-19 00:00:00 |  |
| msc_conviction_date | TIMESTAMP | 72.1% | 2025-11-13 00:00:00 |  |
| felon | VARCHAR | 100.0% |  |  |
| processing_disposition | VARCHAR | 0.0% | Detainer |  |
| case_category | VARCHAR | 49.3% | [8E] Inadmissible - ICE Fugitive |  |
| final_program | VARCHAR | 100.0% |  |  |
| time_of_apprehension_case_category | VARCHAR | 100.0% |  |  |
| time_of_apprehension_current_program | VARCHAR | 100.0% |  |  |
| apprehension_method | VARCHAR | 75.0% | CAP Local Incarceration |  |
| case_final_order_yes_no | VARCHAR | 100.0% |  |  |
| final_order_date | TIMESTAMP | 68.5% | 2015-02-25 00:00:00 |  |
| apprehension_date | TIMESTAMP | 75.0% | 2023-05-11 09:49:00 | Arrest date, joins arrests to detentions by person+date |
| entry_date | TIMESTAMP | 86.7% | 2022-06-01 00:00:00 |  |
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
| biometric_match_yes_no | VARCHAR | 19.6% | NO |  |
| statements_made_yes_no | VARCHAR | 19.6% | NO |  |
| unlawful_attempt_yes_no | VARCHAR | 100.0% | NO |  |
| unlawful_entry_yes_no | VARCHAR | 100.0% | YES |  |
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
| unique_id | VARCHAR | 12.5% | f1bc79f7f98cfff4d16301d12e5f198d6b74b538 | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2026 | Release identifier (release_2023, release_2025, or release_2026) |
| detainer_criminality | VARCHAR | 0.0% | 2 Pending Criminal Charges |  |
| detainer_facility | VARCHAR | 0.0% | GARDENA POLICE DEPT. |  |
| detainer_facility_code | VARCHAR | 0.0% | BOPBIG |  |
| detainer_threat_level | DOUBLE | 6.8% | 1.0 |  |
| msc_charge | VARCHAR | 72.1% | Enticement of Minor for Indecent Purposes |  |
| aggravated_felon_yes_no | VARCHAR | 0.1% | Not an Aggravated Felon |  |
| toa_case_category | VARCHAR | 85.7% | [2A] Deportable - Under Adjudication by IJ |  |
| toa_current_program | VARCHAR | 75.1% | ERO Criminal Alien Program |  |
| federal_register_notice_yes_no | VARCHAR | 42.6% | YES |  |
| detainer_lift_reason_code | VARCHAR | 33.4% | B |  |
| active_investigation_yes_no | VARCHAR | 100.0% | YES |  |
| notify_release_request_yes_no | VARCHAR | 100.0% | NO |  |
| tod_current_duty_site | VARCHAR | 0.1% | ORLANDO, FL, DOCKET CONTROL OFFICE |  |

## detentions

Detention stays (book-in to book-out)

Rows: 9,288,543

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| detention_id | VARCHAR | 26.1% | (b)(6)(b)(7)(c) |  |
| case_id | VARCHAR | 26.9% | (b)(6)(b)(7)(c) | EID case identifier |
| subject_id | VARCHAR | 26.1% | (b)(6)(b)(7)(c) |  |
| stay_book_in_date | TIMESTAMP | 0.0% | 2012-04-07 00:00:00 | Detention start date |
| detention_book_in_date | TIMESTAMP | 0.0% | 2012-04-07 00:00:00 |  |
| detention_facility | VARCHAR | 0.0% | FLORENCE STAGING FACILITY |  |
| detention_facility_code | VARCHAR | 0.0% | OTROPNM | Facility identifier for detention location |
| detention_book_out_date | TIMESTAMP | 26.1% | 2012-06-12 00:00:00 |  |
| detention_release_reason | VARCHAR | 0.6% | Transferred |  |
| stay_book_out_date | TIMESTAMP | 1.7% | 2012-06-12 00:00:00 |  |
| stay_release_reason | VARCHAR | 1.7% | Removed |  |
| religion | VARCHAR | 97.1% | NTA |  |
| marital | VARCHAR | 0.7% | Single |  |
| gender | VARCHAR | 0.0% | Male |  |
| ethnicity | VARCHAR | 54.9% | Hispanic Origin |  |
| alien_file_number | VARCHAR | 26.4% | (b)(6)(b)(7)(c) |  |
| birth_year | DOUBLE | 0.0% | 1990.0 |  |
| entry_status | VARCHAR | 4.7% | PWA Mexico |  |
| bond_posted_date | TIMESTAMP | 87.1% | 2012-05-03 00:00:00 |  |
| bond_posted_amount | DOUBLE | 87.1% | 5000.0 |  |
| initial_bond_set_amount | DOUBLE | 85.7% | 7500.0 |  |
| case_status | VARCHAR | 1.0% | 8-Excluded/Removed - Inadmissibility |  |
| case_category | VARCHAR | 1.0% | [16] Reinstated Final Order |  |
| final_order_yes_no | VARCHAR | 1.0% | YES |  |
| final_order_date | TIMESTAMP | 30.6% | 2013-05-09 00:00:00 |  |
| departed_date | TIMESTAMP | 31.5% | 2016-07-15 00:00:00 |  |
| departure_country | VARCHAR | 31.5% | GUATEMALA |  |
| case_threat_level | DOUBLE | 54.9% | 3.0 |  |
| charge | VARCHAR | 50.2% | IMMIGRANT WITHOUT AN IMMIGRANT VISA |  |
| charge_code | VARCHAR | 50.2% | I7A1 |  |
| charge_section_code | VARCHAR | 50.2% | 212a7AiI |  |
| unique_id | VARCHAR | 0.4% | eab5153b48965fceac6f5ca727a34ae4a2676e2e | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023, release_2025, or release_2026) |
| stay_book_out_date_time | TIMESTAMP | 75.7% | 2025-12-12 17:15:00 |  |
| felon | VARCHAR | 100.0% |  |  |
| book_in_criminality | VARCHAR | 73.9% | 3 Other Immigration Violator |  |
| final_charge | VARCHAR | 81.4% | IMMIGRANT WITHOUT AN IMMIGRANT VISA |  |
| citizenship_country | VARCHAR | 73.9% | ECUADOR |  |
| final_program | VARCHAR | 100.0% |  |  |
| msc_charge_code | VARCHAR | 91.7% | 5707 |  |
| msc_charge | VARCHAR | 91.7% | Assault |  |
| book_out_date_time | TIMESTAMP | 74.6% | 2023-08-09 09:09:00 |  |
| birth_country | VARCHAR | 73.9% | GUATEMALA |  |
| known_terrorist_yes_no | VARCHAR | 73.9% | NO |  |
| suspected_gang_yes_no | VARCHAR | 73.9% | NO |  |
| msc_sentence_days | DOUBLE | 97.2% | 30.0 |  |
| msc_sentence_months | DOUBLE | 98.3% | 97.0 |  |
| msc_sentence_years | DOUBLE | 98.5% | 4.0 |  |
| aggravated_felon_yes_no | VARCHAR | 87.1% | Not an Aggravated Felon |  |
| offense_ina_236c_yes_no | VARCHAR | 74.7% | N |  |
| case_ina_236c_yes_no | VARCHAR | 74.1% | N |  |
| detainee_classification | VARCHAR | 73.9% | Low |  |
| initial_bond_set_date | TIMESTAMP | 99.8% | 2019-09-05 00:00:00 |  |
| race | VARCHAR | 74.3% | White |  |
| entry_date | TIMESTAMP | 84.3% | 2023-05-20 00:00:00 |  |
| apprehension_final_program | VARCHAR | 74.7% | Border Patrol |  |
| msc_charge_date | TIMESTAMP | 91.9% | 2024-06-23 00:00:00 |  |
| msc_conviction_date | TIMESTAMP | 91.7% | 2022-11-02 00:00:00 |  |
| msc_criminal_charge_status | VARCHAR | 91.7% | Convicted |  |
| msc_criminal_charge_status_code | VARCHAR | 91.7% | C |  |
| msc_crime_class | VARCHAR | 92.0% | Felony |  |
| book_in_site | VARCHAR | 73.9% | OAKDALE PROCESSING CENTER FEDERAL ALIEN DETENTION FACILITY |  |
| book_in_aor | VARCHAR | 73.9% | New Orleans Area of Responsibility |  |

## encounters

ICE encounters with individuals

Rows: 2,586,515

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| event_date | TIMESTAMP | 0.0% | 2023-02-13 09:29:00 |  |
| event_type | VARCHAR | 0.0% | CAP Local |  |
| event_landmark | VARCHAR | 55.4% | HILLSBOROUGH COUNTY DOC |  |
| operation | VARCHAR | 89.2% | - |  |
| encounter_threat_level | VARCHAR | 67.6% | 1 |  |
| responsible_aor | VARCHAR | 2.5% | Boston Area of Responsibility |  |
| responsible_site | VARCHAR | 0.0% | BOSTON, MA, DOCKET CONTROL OFFICE |  |
| lead_event_type | VARCHAR | 0.0% | CAP Local |  |
| lead_source | VARCHAR | 84.3% | Other Lead |  |
| final_program | VARCHAR | 0.0% | ERO Criminal Alien Program |  |
| arresting_agency | VARCHAR | 0.0% | ICE |  |
| encounter_criminality | VARCHAR | 0.0% | 3 Other Immigration Violator |  |
| processing_disposition | VARCHAR | 0.1% | Not Amenable to Removal |  |
| case_status | VARCHAR | 52.0% | 6-Deported/Removed - Deportability |  |
| case_category | VARCHAR | 52.0% | [16] Reinstated Final Order |  |
| departed_date | TIMESTAMP | 78.0% | 2023-06-26 00:00:00 |  |
| departure_country | VARCHAR | 78.0% | MEXICO |  |
| final_order_yes_no | VARCHAR | 52.0% | YES |  |
| final_order_date | TIMESTAMP | 77.9% | 2012-10-05 00:00:00 |  |
| birth_year | DOUBLE | 0.2% | 1989.0 |  |
| citizenship_county | VARCHAR | 0.0% | UNKNOWN |  |
| gender | VARCHAR | 0.0% | Male |  |
| unique_id | VARCHAR | 10.8% | fbff7a7a5057103e4825275c297a479d449353e9 | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2026 | Release identifier (release_2023, release_2025, or release_2026) |

## rca_decisions

Release/custody assessment decision history

Rows: 3,543,467

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| rca_aor | VARCHAR | 0.0% | NOL |  |
| rca_dco | VARCHAR | 0.0% | BAL |  |
| a_number | VARCHAR | 0.3% | b(6), b(7)(c) |  |
| subj_id | VARCHAR | 10.0% | b(6), b(7)(c) |  |
| last_name | VARCHAR | 0.0% | b(6), b(7)(c) |  |
| first_name | VARCHAR | 0.0% | b(6), b(7)(c) |  |
| alert_code | VARCHAR | 56.5% | 2, M |  |
| active_inactive | VARCHAR | 0.0% | Active |  |
| submission_date | TIMESTAMP | 16.1% | 2015-05-11 00:00:00 |  |
| status_code | VARCHAR | 26.1% | C |  |
| risk_to_public_safety | VARCHAR | 16.1% | Low |  |
| risk_of_flight | VARCHAR | 16.1% | Medium |  |
| special_vulnerability | VARCHAR | 17.9% | NONE |  |
| rca_case_number | VARCHAR | 68.6% | b(7)(e) |  |
| case_cat_at_rca_decision | VARCHAR | 68.6% | 5B |  |
| fo_at_rca_decision | VARCHAR | 0.0% | Y |  |
| fo_date_at_rca_decision | TIMESTAMP | 70.4% | 2004-09-23 00:00:00 |  |
| removal_likely_at_rca_decision | VARCHAR | 89.4% | Y |  |
| man_det_per_stat_alleg | VARCHAR | 31.4% | N |  |
| rca_decision_type | VARCHAR | 0.0% | Detain/Release  |  |
| rca_recommendation | VARCHAR | 0.0% | Supervisor to Determine - Detain or Release on Community Supervision |  |
| rca_bond_recommendation | DOUBLE | 93.6% | 4000.0 |  |
| officer_id | VARCHAR | 16.1% | b(6), b(7)(c)   |  |
| officer_agree_disagree | VARCHAR | 16.1% | Not Applicable, Supervisor to Determine |  |
| supervisor_id | VARCHAR | 1.8% | b(6), b(7)(c) |  |
| supervisor_agree_disagree | VARCHAR | 0.0% | Not Applicable, Supervisor to Determine |  |
| rca_final_decision | VARCHAR | 0.0% | Detain in the Custody of This Service |  |
| final_bond_amount | DOUBLE | 98.0% | 9000.0 |  |
| rca_decision_date | TIMESTAMP | 0.0% | 2015-05-11 00:00:00 |  |
| rca_scoring_ver | DOUBLE | 16.1% | 1.2 |  |
| spec_vuln_ver | DOUBLE | 16.1% | 1.0 |  |
| man_det_ver | DOUBLE | 91.9% | 1.0 |  |
| disc_infr_ver | DOUBLE | 99.8% | 1.0 |  |
| fiscal_year_code | BIGINT | 0.0% | 2013 |  |
| fiscal_quarter_name | VARCHAR | 0.0% | Q4 |  |
| unique_id | VARCHAR | 0.3% | 0423d85cb15c74d429f83f123824ff3a06dbc718 | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023, release_2025, or release_2026) |
| special_vulnerability_comments | VARCHAR | 99.6% | b(6), b(7)(c) |  |
| reason_removal_unlikely_at_rca_decision | VARCHAR | 99.4% | Expressed Fear of Returning to His/Her Country |  |
| officer_comments | VARCHAR | 97.3% | b(6), b(7)(c) |  |
| supervisor_comments | VARCHAR | 96.7% | b(6), b(7)(c) |  |
| sujb_id | VARCHAR | 90.0% | (b)(6),(b)(7)(c) |  |

## removals

Deportation/removal records

Rows: 3,680,770

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| departure_date | TIMESTAMP | 0.0% | 2013-01-22 00:00:00 | Removal/departure date |
| port_of_departure | VARCHAR | 0.0% | MIAMI INTERNATIONAL AIRPORT, MIAMI FLORIDA, POE |  |
| departure_country | VARCHAR | 0.0% | MEXICO |  |
| case_status | VARCHAR | 0.0% | 6-Deported/Removed - Deportability |  |
| case_category | VARCHAR | 0.0% | [16] Reinstated Final Order |  |
| final_order_yes_no | VARCHAR | 0.0% | YES |  |
| final_order_date | TIMESTAMP | 9.7% | 2006-10-06 00:00:00 |  |
| case_id | VARCHAR | 28.6% | (b)(6),(b)(7)(c) | EID case identifier |
| gender | VARCHAR | 0.0% | Male |  |
| birth_country | VARCHAR | 0.0% | MEXICO |  |
| citizenship_country | VARCHAR | 0.0% | MEXICO |  |
| birth_year | DOUBLE | 0.0% | 1970.0 |  |
| alien_file_number | VARCHAR | 28.9% | (b)(6),(b)(7)(c) |  |
| entry_status | VARCHAR | 1.6% | PWA Mexico |  |
| entry_date | TIMESTAMP | 25.0% | 2006-09-11 00:00:00 |  |
| msc_charge | VARCHAR | 51.3% | Illegal Entry (INA SEC.101(a)(43)(O), 8USC1325 only) |  |
| msc_charge_date | TIMESTAMP | 53.5% | 2007-08-15 00:00:00 |  |
| msc_charge_code | VARCHAR | 51.3% | 0999 |  |
| msc_conviction_date | TIMESTAMP | 51.3% | 2009-07-12 00:00:00 |  |
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
| case_aor | VARCHAR | 71.4% | San Antonio Area of Responsibility |  |
| state | VARCHAR | 93.6% | GEORGIA |  |
| county | VARCHAR | 100.0% | LOS ANGELES |  |
| known_terrorist_yes_no | VARCHAR | 71.4% | NO |  |
| suspected_gang_yes_no | VARCHAR | 71.4% | NO |  |
| case_criminality | VARCHAR | 71.4% | 1 Convicted Criminal |  |
| aggravated_felon_yes_no | VARCHAR | 88.1% | Not an Aggravated Felon |  |
| final_program | VARCHAR | 71.4% | ERO Criminal Alien Program |  |
| final_program_code | VARCHAR | 71.4% | CAP |  |
| arresting_agency | VARCHAR | 71.4% | ICE |  |
| toa_case_category | VARCHAR | 95.5% | [16] Reinstated Final Order |  |
| latest_apprehension_final_program | VARCHAR | 71.6% | ERO Criminal Alien Program |  |
| latest_arresting_agency | VARCHAR | 71.6% | ICE |  |
| latest_apprehension_date | TIMESTAMP | 71.6% | 2023-11-29 11:35:00 |  |
| final_charge_code | VARCHAR | 71.4% | I6A |  |
| final_charge_section | VARCHAR | 71.4% | 212a6Ai |  |
| prior_deport_yes_no | VARCHAR | 71.4% | NO |  |

## v_arrest_to_detention

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| apprehension_date | TIMESTAMP | 0.0% | 2015-10-18 00:00:00 | Arrest date, joins arrests to detentions by person+date |
| apprehension_method | VARCHAR | 0.0% | Non-Custodial Arrest |  |
| arrest_created_by | VARCHAR | 30.4% | (b)(6)(b)(7)(c) |  |
| case_id | VARCHAR | 32.5% | (b)(6)(b)(7)(c) | EID case identifier |
| subject_id | VARCHAR | 30.4% | (b)(6)(b)(7)(c) |  |
| alien_file_number | VARCHAR | 31.1% | (b)(6)(b)(7)(c) |  |
| unique_id | VARCHAR | 1.3% | f63a20964b0517a2d14496e4323303288699a377 | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023, release_2025, or release_2026) |
| apprehension_state | VARCHAR | 100.0% |  |  |
| apprehension_aor | VARCHAR | 100.0% |  |  |
| final_program | VARCHAR | 100.0% |  |  |
| final_program_group | VARCHAR | 100.0% |  |  |
| apprehension_criminality | VARCHAR | 69.6% | 3 Other Immigration Violator |  |
| case_status | VARCHAR | 70.4% | 9-VR Witnessed |  |
| case_category | VARCHAR | 70.4% | [3] Deportable - Administratively Final Order |  |
| departed_date | TIMESTAMP | 81.3% | 2023-01-16 00:00:00 |  |
| departure_country | VARCHAR | 81.3% | MEXICO |  |
| final_order_yes_no | VARCHAR | 70.4% | NO |  |
| final_order_date | TIMESTAMP | 83.4% | 2023-01-11 00:00:00 |  |
| birth_year | DOUBLE | 69.6% | 1971.0 |  |
| citizenship_country | VARCHAR | 69.6% | CUBA |  |
| gender | VARCHAR | 69.6% | Male |  |
| apprehension_site_landmark | VARCHAR | 70.2% | FEDERAL CORRECTIONAL INSTITUTE - OAKDALE |  |
| apprehension_type | VARCHAR | 89.5% | Targeted |  |
| state | VARCHAR | 74.1% | TEXAS |  |
| toa_current_duty_aor | VARCHAR | 69.9% | New Orleans Area of Responsibility |  |
| apprehension_final_program | VARCHAR | 69.6% | Non-Detained Docket Control |  |
| arresting_agency | VARCHAR | 69.6% | ICE |  |
| operation | VARCHAR | 92.4% | SBI |  |
| toa_current_duty_site | VARCHAR | 69.6% | HOUSTON, TX, DOCKET CONTROL OFFICE |  |
| case_criminality | VARCHAR | 70.4% | 2 Pending Criminal Charges |  |
| case_threat_level | DOUBLE | 88.9% | 1.0 |  |
| stay_book_in_date | TIMESTAMP | 21.7% | 2015-12-10 00:00:00 | Detention start date |
| stay_book_out_date | TIMESTAMP | 23.8% | 2019-01-18 00:00:00 |  |
| stay_release_reason | VARCHAR | 23.8% | Bonded Out |  |
| initial_detention_facility | VARCHAR | 21.7% | LOS CUST CASE |  |
| days_arrest_to_detention | BIGINT | 21.7% | 0 |  |
| days_in_detention | BIGINT | 23.8% | 0 |  |

## v_daily_arrests

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| date | DATE | 0.0% | 2011-10-01 |  |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023, release_2025, or release_2026) |
| arrest_count | BIGINT | 0.0% | 142 |  |

## v_detention_stays

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unique_id | VARCHAR | 0.2% | b4f81c87fdbec691f17badf13f49902b4c5bc0da | Anonymized person ID, links across arrests, detainers, detentions, removals |
| data_source | VARCHAR | 0.0% | release_2023 | Release identifier (release_2023, release_2025, or release_2026) |
| stay_book_in_date | TIMESTAMP | 0.0% | 2013-07-19 00:00:00 | Detention start date |
| stay_book_out_date | TIMESTAMP | 1.3% | 2012-03-05 00:00:00 |  |
| stay_release_reason | VARCHAR | 1.3% | Removed |  |
| initial_detention_facility | VARCHAR | 0.0% | LEXINGTON COUNTY JAIL |  |
| facility_segments | BIGINT | 0.0% | 1 |  |

## v_enforcement_pipeline

| Column | Type | Nulls | Example | Join |
|--------|------|-------|---------|------|
| unique_id | VARCHAR | 1.3% | 5b116f1f3bdfc3904084913ddf8ed2f1e67ef058 | Anonymized person ID, links across arrests, detainers, detentions, removals |
| apprehension_date | TIMESTAMP | 0.0% | 2014-10-22 00:00:00 | Arrest date, joins arrests to detentions by person+date |
| arrest_source | VARCHAR | 0.0% | release_2023 |  |
| stay_book_in_date | TIMESTAMP | 21.7% | 2015-12-10 00:00:00 | Detention start date |
| stay_book_out_date | TIMESTAMP | 23.8% | 2016-07-12 00:00:00 |  |
| detention_facility | VARCHAR | 21.7% | YORK COUNTY JAIL, PA |  |
| departure_date | TIMESTAMP | 34.6% | 2017-05-16 00:00:00 | Removal/departure date |
| removal_country | VARCHAR | 34.6% | MEXICO |  |
| days_to_detention | BIGINT | 21.7% | 0 |  |
| days_detained | BIGINT | 23.8% | 17 |  |
| days_to_removal | BIGINT | 34.6% | 166 |  |
