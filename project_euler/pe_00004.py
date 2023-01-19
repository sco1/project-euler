"""
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two
2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import itertools


def largest_palindrome_product(n_digits: int = 3) -> int:  # noqa: D103
    largest_prod = -1
    for a, b in itertools.combinations(range(10 ** (n_digits - 1), 10**n_digits), 2):
        str_prod = str(a * b)
        if str_prod == str_prod[::-1]:
            largest_prod = max(largest_prod, a * b)

    return largest_prod


if __name__ == "__main__":
    print(f"Solution: {largest_palindrome_product()}")
