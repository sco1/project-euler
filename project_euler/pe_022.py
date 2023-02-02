"""
Names scores
https://projecteuler.net/problem=22

Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name, multiply this value by
its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth
3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of
938 x 53 = 49714.

What is the total of all the name scores in the file?
"""
import string
import typing as t
from pathlib import Path

NAME_FILE = Path(__file__).parent / "data" / "p022_names.txt"

SCORING_RUBRIC = {letter: score for score, letter in enumerate(string.ascii_uppercase, start=1)}


def score_name(name: str, idx: int) -> int:
    """
    Calculate the score of the provided name.

    A name's score is determined by multiplying the sum of its letter indices by its index in the
    names list.
    """
    name = name.upper()
    return idx * sum((SCORING_RUBRIC[c] for c in name))


def total_name_score(names: t.Iterable[str]) -> int:  # pragma: no cover
    """
    Calculate the total score of the provided names list.

    A name's score is determined by multiplying the sum of its letter indices by its index in the
    sorted names list.
    """
    names = sorted(names)
    return sum((score_name(name, idx) for idx, name in enumerate(names, start=1)))


def test_score_name() -> None:
    assert score_name("COLIN", 938) == 49_714


if __name__ == "__main__":
    names = (name.strip('"') for name in NAME_FILE.read_text().split(","))
    print(f"Solution: {total_name_score(names)}")
