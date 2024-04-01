"""
Lexicographic permutations
https://projecteuler.net/problem=24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of
the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we
call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import itertools
import typing as t


def nth_permutation(
    digits: t.Iterable[str] = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"),
    n: int = 1_000_000,
) -> str:
    for idx, comb in enumerate(itertools.permutations(digits), start=1):
        if idx == n:
            return "".join(comb)

    raise ValueError("Could not form enough permutations of the given digits.")


if __name__ == "__main__":
    print(f"Solution: {nth_permutation()}")
