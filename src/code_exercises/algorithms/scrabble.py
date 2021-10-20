
'''
The Goal
When playing Scrabble©, each player draws 7 letters and must find a word
that scores the most points using these letters.

A player doesn't necessarily have to make a 7-letter word; the word can be
shorter. The only constraint is that the word must be made using the 7
letters which the player has drawn.

For example, with the letters  etaenhs, some possible words are: ethane,
hates, sane, ant.

Your objective is to find the word that scores the most points using the
available letters (1 to 7 letters).

 Rules
In Scrabble©, each letter is weighted with a score depending on how difficult
it is to place that letter in a word. You will see below a table showing the
points corresponding to each letter:
 

Letters	Points
e, a, i, o, n, r, t, l, s, u	1
d, g	2
b, c, m, p	3
f, h, v, w, y	4
k	5
j, x	8
q, z	10
The word banjo earns you 3 + 1 + 1 + 8 + 1 = 14 points.

A dictionary of authorized words is provided as input for the program. The
program must find the word in the dictionary which wins the most points for
the seven given letters (a letter can only be used once). If two words win
the same number of points, then the word which appears first in the order of
the given dictionary should be chosen.
 

All words will only be composed of alphabetical characters in lower case.
There will always be at least one possible word.
'''


def scrabble_input():
    I = input
    words = [I() for i in range(int(I()))]
    letters = I()
    return words, letters


def scrabble_score(word, letters):
    values = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4,
              "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
              "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}

    FilteredValues = {k: v for (k, v) in values.items() if k in letters}
    result = 0
    used = []
    for letter in word:
        if letter not in used:
            try:
                result += FilteredValues[letter]
            except KeyError:
                result -= 1000
        else:
            result -= 1000
        used.append(letter)
    return result


def scrabble():
    words, letters = scrabble_input()
    score = [scrabble_score(word, letters) for word in words]
    print(words[score.index(max(score))])


if __name__ == '__main__':
    scrabble()
