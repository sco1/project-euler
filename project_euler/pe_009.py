"""
Special Pythagorean triplet
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import itertools

import pytest


def special_pythagorean_triplet(target: int = 1000) -> int:
    # Diving into the equation a bit, we know that c = target - (a + b)
    # We also know that c has to be greater than a and b (remember triangle sides)
    # Without getting into smarter math, this gives us an upper bound on the values of a and b of
    # target / 2, which allows us to limit our brute force.
    #
    # I'm assuming we could do something with Euclid's formula, but the brute force is adequate here
    # See: https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples
    for a, b in itertools.combinations(range(1, target // 2 + 1), 2):
        c = target - (a + b)
        if c < a or c < b:
            continue

        if (a**2 + b**2) == c**2:
            return a * b * c

    raise ValueError("Could not determine a triplet matching the provided target.")


def test_pythagorean_triplet() -> None:
    assert special_pythagorean_triplet(12) == 60


@pytest.mark.parametrize("target", (-10, 10))
def test_unreachable_target_raises(target: int) -> None:
    with pytest.raises(ValueError):
        special_pythagorean_triplet(target)


if __name__ == "__main__":
    print(f"Solution: {special_pythagorean_triplet()}")
