"""
Non-abundant sums
https://projecteuler.net/problem=23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the
number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which
means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called
abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be
written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all
integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper
limit cannot be reduced any further by analysis even though it is known that the greatest number
that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant
numbers.
"""
import itertools

from helpers.matlib import proper_divisors

ABUNDANT_FLOOR = 28_123


def is_abundant(n: int) -> bool:
    """
    Determine if the provided number is abundant.

    A number is considered abundent if the sum of its proper divisors exceeds the number.
    """
    return sum(proper_divisors(n)) > n


def sum_non_abundant() -> int:  # pragma: no cover
    # Since we know what the maximum possible sum could be from 1 to n, we can subtract from this
    # the sum of all the numbers that we can calculate as the sum of 2 abundant numbers, which will
    # leave us with the sum of all the numbers that cannot.
    abundants = (i for i in range(ABUNDANT_FLOOR + 1) if is_abundant(i))

    expressible = set()
    for pair in itertools.combinations_with_replacement(abundants, 2):
        pair_sum = sum(pair)
        if pair_sum <= ABUNDANT_FLOOR:
            expressible.add(pair_sum)

    # Sum of numbers 1..n is n(n+1)/2
    max_sum = (ABUNDANT_FLOOR * (ABUNDANT_FLOOR + 1)) // 2
    return max_sum - sum(expressible)


def test_is_abundant() -> None:
    assert is_abundant(12)


if __name__ == "__main__":
    print(f"Solution: {sum_non_abundant()}")
