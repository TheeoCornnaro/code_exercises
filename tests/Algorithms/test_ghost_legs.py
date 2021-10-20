from src.code_exercises.algorithms.ghost_legs import ghost_legs
from pathlib import Path
import json
import pytest
import mock


# Importing Test Data - Structure -> [inputs], output
base_path = Path(__file__).parent
with open(base_path / 'json/ghost_legs_data.json', 'r') as f:
    test_data = json.load(f)

# Test


@ pytest.mark.parametrize('input, output', test_data)
def test_ghost_legs(monkeypatch, capfd, input, output):
    with mock.patch('builtins.input', side_effect=input):
        ghost_legs()
    out, err = capfd.readouterr()
    assert out == output


if __name__ == '__main__':
    pytest.main()
