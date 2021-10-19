import pytest
import mock
from src.code_exercises import ghost_legs


test_samples = [
    ([
        '7 7',
        'A  B  C',
        '|  |  |',
        '|--|  |',
        '|  |--|',
        '|  |--|',
        '|  |  |',
        '1  2  3'],
        'A2\nB1\nC3\n'),
    ([
        '13 8',
        'A  B  C  D  E',
        '|  |  |  |  |',
        '|  |--|  |  |',
        '|--|  |  |  |',
        '|  |  |--|  |',
        '|  |--|  |--|',
        '|  |  |  |  |',
        '1  2  3  4  5'],
        'A3\nB5\nC1\nD2\nE4\n'),
    ([
        '16 14',
        'F  E  D  C  B  A',
        '|  |--|  |  |  |',
        '|--|  |--|  |--|',
        '|  |--|  |--|  |',
        '|  |  |  |  |--|',
        '|  |--|  |--|  |',
        '|  |  |--|  |  |',
        '|  |  |--|  |--|',
        '|--|  |  |--|  |',
        '|  |  |--|  |  |',
        '|--|  |  |  |--|',
        '|  |--|  |  |  |',
        '|  |  |--|  |  |',
        '0  1  2  3  4  5'],
     'F3\nE1\nD0\nC2\nB5\nA4\n'),
    ([
        '22 18',
        'P  Q  R  S  T  U  V  W',
        '|  |  |  |  |--|  |  |',
        '|  |  |--|  |  |  |--|',
        '|  |--|  |--|  |  |  |',
        '|--|  |--|  |  |  |--|',
        '|--|  |  |  |  |--|  |',
        '|  |--|  |  |--|  |--|',
        '|  |  |  |--|  |--|  |',
        '|--|  |  |  |--|  |  |',
        '|  |  |--|  |  |  |  |',
        '|  |  |  |--|  |  |--|',
        '|  |  |  |  |--|  |  |',
        '|--|  |  |  |  |  |  |',
        '|--|  |--|  |  |  |--|',
        '|  |--|  |  |--|  |  |',
        '|  |  |--|  |  |  |--|',
        '|--|  |--|  |  |--|  |',
        '1  2  3  4  5  6  7  8', ],
     'P3\nQ7\nR8\nS5\nT6\nU2\nV4\nW1\n'),
    ([
        '28 20', 'A  B  C  D  E  F  G  H  I  J',
        '|--|  |--|  |--|  |--|  |--|',
        '|  |--|  |--|  |--|  |--|  |',
        '|--|  |--|  |--|  |--|  |--|',
        '|--|  |--|  |--|  |--|  |--|',
        '|  |--|  |--|  |--|  |--|  |',
        '|  |--|  |--|  |--|  |--|  |',
        '|--|  |--|  |--|  |--|  |--|',
        '|--|  |--|  |--|  |--|  |--|',
        '|  |--|  |--|  |--|  |--|  |',
        '|--|  |--|  |--|  |--|  |--|',
        '|  |--|  |--|  |--|  |--|  |',
        '|--|  |--|  |--|  |--|  |--|',
        '|--|  |--|  |--|  |--|  |--|',
        '|--|  |--|  |--|  |--|  |--|',
        '|  |--|  |--|  |--|  |--|  |',
        '|--|  |--|  |--|  |--|  |--|',
        '|--|  |--|  |--|  |--|  |--|',
        '|  |--|  |--|  |--|  |--|  |',
        '0  1  2  3  4  5  6  7  8  9'],
     'A1\nB3\nC0\nD5\nE2\nF7\nG4\nH9\nI6\nJ8\n'),
    ([
        '76 23',
        '~  !  @  #  $  %  ^  &  *  (  )  +  `  1  2  3  4  5  6  7  8  9  0  =  \  /',
        '|  |--|  |  |--|  |  |--|  |--|  |  |--|  |  |  |--|  |--|  |  |--|  |  |--|',
        '|--|  |--|  |  |  |--|  |--|  |--|  |  |  |--|  |  |--|  |--|  |  |  |--|  |',
        '|  |--|  |--|  |  |  |  |  |--|  |--|  |  |  |  |--|  |--|  |--|  |--|  |--|',
        '|--|  |--|  |  |  |--|  |--|  |--|  |  |  |--|  |--|  |--|  |  |  |--|  |--|',
        '|--|  |  |  |  |--|  |  |--|  |  |  |  |--|  |--|  |--|  |--|  |--|  |--|  |',
        '|  |--|  |  |--|  |--|  |  |--|  |  |--|  |--|  |  |  |--|  |  |--|  |--|  |',
        '|  |  |  |--|  |--|  |--|  |  |  |--|  |--|  |  |--|  |--|  |--|  |--|  |--|',
        '|--|  |  |  |--|  |--|  |--|  |  |  |--|  |--|  |--|  |  |--|  |  |--|  |--|',
        '|  |  |--|  |  |  |  |--|  |  |--|  |  |  |  |  |  |--|  |  |  |--|  |--|  |',
        '|  |  |  |--|  |  |--|  |  |  |  |--|  |  |--|  |--|  |--|  |--|  |--|  |--|',
        '|  |--|  |--|  |  |  |  |  |--|  |--|  |  |  |  |--|  |--|  |--|  |--|  |--|',
        '|--|  |--|  |  |  |--|  |--|  |--|  |  |  |--|  |--|  |--|  |  |  |--|  |--|',
        '|--|  |  |  |  |--|  |  |--|  |  |  |  |--|  |--|  |--|  |--|  |--|  |--|  |',
        '|--|  |--|  |  |  |--|  |--|  |--|  |  |  |--|  |  |--|  |  |  |--|  |  |--|',
        '|  |--|  |  |--|  |--|  |  |--|  |  |--|  |--|  |  |  |--|  |  |--|  |--|  |',
        '|  |--|  |  |--|  |  |  |  |--|  |  |--|  |  |--|  |--|  |--|  |--|  |--|  |',
        '|--|  |  |--|  |  |  |  |--|  |  |--|  |--|  |  |--|  |--|  |--|  |--|  |--|',
        '|--|  |--|  |  |  |--|  |--|  |--|  |  |  |--|  |  |--|  |  |  |--|  |  |--|',
        '|  |--|  |  |--|  |  |--|  |--|  |  |  |--|  |--|  |  |--|  |--|  |--|  |--|',
        '|  |  |  |--|  |  |--|  |  |  |  |--|  |  |--|  |  |--|  |--|  |--|  |--|  |',
        '|--|  |--|  |--|  |--|  |--|  |--|  |--|  |--|  |--|  |--|  |  |  |  |  |--|',
        'a  A  b  B  c  C  d  D  e  E  f  F  g  G  h  H  i  I  j  J  k  K  l  L  m  M'],
     '~E\n!F\n@C\n#c\n$G\n%B\n^A\n&h\n*a\n(g\n)b\n+f\n`I\n1d\n2D\n3i\n4J\n5e\n6M\n7k\n8L\n9l\n0H\n=K\n\j\n/m\n'
     )
]


# Test
@ pytest.mark.parametrize('input, output', test_samples)
def test_ghost_legs(monkeypatch, capfd, input, output):
    with mock.patch('builtins.input', side_effect=input):
        ghost_legs()
    out, err = capfd.readouterr()
    assert out == output


if __name__ == '__main__':
    pytest.main()
