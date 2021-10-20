from src.code_exercises.algorithms import scrabble
from pathlib import Path
import json
import pytest
import mock


# Importing Test Data - Structure -> [inputs], output
base_path = Path(__file__).parent
with open(base_path / 'json/scrabble_data.json', 'r') as f:
    test_data = json.load(f)

# Test Parametrization


@ pytest.mark.parametrize('input, output', test_data)
def test_scrabble(monkeypatch, capfd, input, output):
    with mock.patch('builtins.input', side_effect=input):
        t = scrabble()
    out, err = capfd.readouterr()
    assert out == output


# execute test
if __name__ == '__main__':
    pytest.main()
