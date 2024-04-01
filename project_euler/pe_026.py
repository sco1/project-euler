"""
Reciprocal cycles
Problem 26

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with
denominators 2 to 10 are given:

1/2  = 0.5
1/3  = 0.(3)
1/4  = 0.25
1/5  = 0.2
1/6  = 0.1(6)
1/7  = 0.(142857)
1/8  = 0.125
1/9  = 0.(1)
1/10 = 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a
6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal
fraction part.
"""

import pytest


def len_recurring_cycle(n: int) -> int:
    """Calculate the length of the recurring cycle of `1/n`."""
    # Time for some manual long division!
    seen: set[int] = set()
    numerator = 10
    while True:
        numerator = (numerator % n) * 10
        if numerator == 0:
            return 0

        if numerator in seen:
            return len(seen)
        else:
            seen.add(numerator)


def find_logest_recurring_cycle(limit: int = 1000) -> int:
    """Locate the value `x` below `limit` such that 1/`x` gives the longest recurring cycle."""
    return max(range(1, limit), key=len_recurring_cycle)


TEST_CASES = (
    (2, 0),
    (3, 1),
    (4, 0),
    (6, 1),
    (7, 6),
)


@pytest.mark.parametrize(("n", "truth_len"), TEST_CASES)
def test_len_recurring_cycle(n: int, truth_len: int) -> None:
    assert len_recurring_cycle(n) == truth_len


def test_find_longest_recurring_cycle() -> None:
    assert find_logest_recurring_cycle(10) == 7


if __name__ == "__main__":
    print(f"Solution: {find_logest_recurring_cycle()}")
