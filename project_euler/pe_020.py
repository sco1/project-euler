"""
Factorial digit sum
https://projecteuler.net/problem=20

n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800, and the sum of the digits in the number 10!
is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
import math


def factorial_digit_sum(n: int = 100) -> int:
    """Calculate the sum of the digits of `n!`."""
    # Since Python has no issue with large ints, we can just use the factorial directly
    total = math.factorial(n)
    return sum((int(c) for c in str(total)))


def test_factorial_digit_sum() -> None:
    assert factorial_digit_sum(10) == 27


if __name__ == "__main__":
    print(f"Solution: {factorial_digit_sum()}")
