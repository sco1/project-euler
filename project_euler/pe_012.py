"""
Highly divisible triangular number
https://projecteuler.net/problem=12

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle
number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""
import math

import pytest

from helpers.matlib import triangle_numbers


def n_divisors_brute(val: int) -> int:
    limit = math.isqrt(val)
    n_divisors = sum(2 for check in range(1, limit + 1) if val % check == 0)

    if limit**2 == val:
        n_divisors -= 1

    return n_divisors


def find_highly_divisible(n: int = 500) -> int:
    """Locate the first triangular number with more than `n` divisors."""
    for num in triangle_numbers():  # pragma: no branch
        if n_divisors_brute(num) > n:
            return num

    raise ValueError("Unreachable!")  # pragma: no cover


N_DIVISORS_CASES = (
    (1, 1),
    (3, 2),
    (6, 4),
    (10, 4),
    (15, 4),
    (21, 4),
    (28, 6),
)


@pytest.mark.parametrize(("val", "truth_n"), N_DIVISORS_CASES)
def test_n_divisors_brute(val: int, truth_n: int) -> None:
    assert n_divisors_brute(val) == truth_n


def test_highly_divisible() -> None:
    assert find_highly_divisible(5) == 28


if __name__ == "__main__":
    print(f"Solution: {find_highly_divisible()}")