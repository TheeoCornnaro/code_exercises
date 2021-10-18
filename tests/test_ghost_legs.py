import pytest
import mock
import builtins
from src.code_exercises.ghost_legs import ghost_legs


def gen_inputs():
    inputs = ['7 3', 'A  B  C', '|  |  |', '1  2  3']
    for i in inputs:
        yield i


GEN = gen_inputs()


def test_ghost_legs(monkeypatch, capfd):
    monkeypatch.setattr('builtins.input', lambda: next(GEN))
    ghost_legs()
    out, err = capfd.readouterr()
    assert out == 'A1\nB2\nC3\n'
