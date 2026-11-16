"""Offline checks for generated provenance and executable example syntax."""
import ast
import re

import duckdb

from publish_to_hf import generate_dataset_card


def test_card_preserves_current_source_and_count_semantics(tmp_path):
    path = tmp_path / 'fixture.duckdb'
    with duckdb.connect(str(path), config={'threads': '1', 'memory_limit': '128MiB'}) as con:
        con.execute('CREATE TABLE _metadata(table_name VARCHAR, description VARCHAR, row_count BIGINT, column_count INTEGER, data_sources VARCHAR, date_range VARCHAR)')
        con.execute("INSERT INTO _metadata VALUES ('arrests','arrest',2516550,25,'release_2023, release_2026_08','2011-10-01 to 2026-08-06'), ('rca_decisions','historical RCA',3543467,42,'release_2023',''), ('detentions','Detention stays',9834781,20,'release_2023, release_2026_08','')")
    card = generate_dataset_card(str(path))
    assert '**15,894,798 rows** across **3 tables**' in card
    assert '| `detentions` | Detention facility segments | 9,834,781 |' in card
    assert '| `detentions` | Detention stays |' not in card
    assert 'legacy "Detention stays" description in `_metadata`' in card
    assert 'this card does not rewrite that database' in card
    assert 'August 2026 cumulative release' in card
    assert '`release_2023` or `release_2026_08`' in card
    assert 'IDs are re-anonymized across releases' in card
    assert 'Cross-release overlap is removed by time-window supersession' in card
    assert 'preferring the richer 2025' not in card
    assert 'facility segments, not unique stays' in card
    snippets = re.findall(r'```python\n(.*?)\n```', card, re.S)
    assert len(snippets) == 1
    ast.parse(snippets[0])  # Previously invalid backslash-escaped triple quotes.
    assert '"threads": "1"' in snippets[0] and 'finally:' in snippets[0]
