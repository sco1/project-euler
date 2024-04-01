"""
Amicable numbers
https://projecteuler.net/problem=21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly
into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are
called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore
d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from functools import lru_cache

import pytest

from helpers.matlib import proper_divisors


@lru_cache()
def sum_divisors(n: int) -> int:
    return sum(proper_divisors(n))


def sum_amicable_numbers(limit: int = 10_000) -> int:  # pragma: no cover
    """
    Calculate the sum of all amicable numbers below the provided limit.

    Two numbers are considered amicable if the sum of their proper divisors are inverse of each
    other, e.g. 220 and 284.
    """
    # I'm not sure how to do this without brute-forcing, so we'll try that first!
    amicable_sum = 0
    for n in range(limit):
        sum_div = sum_divisors(n)
        if sum_div != n:
            check_sum = sum_divisors(sum_div)
            if check_sum == n:
                amicable_sum += check_sum

    return amicable_sum


TEST_CASES = (
    (220, 284),
    (284, 220),
)


@pytest.mark.parametrize(("limit", "truth_sum"), TEST_CASES)
def test_sum_divisors(limit: int, truth_sum: int) -> None:
    assert sum_divisors(limit) == truth_sum


if __name__ == "__main__":
    print(f"Solution: {sum_amicable_numbers()}")
