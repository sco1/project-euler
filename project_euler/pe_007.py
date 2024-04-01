"""
10001st prime
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""

import pytest

from helpers.matlib import estimate_prime, sieve_of_eratosthenes


def nth_prime(n: int = 10_001) -> int:
    u_bound = estimate_prime(n)
    sieved = sieve_of_eratosthenes(u_bound)
    for _ in range(n):
        nth = next(sieved)

    return nth


PRIME_CASES = (
    (1, 2),
    (2, 3),
    (3, 5),
    (4, 7),
    (5, 11),
    (6, 13),
    (10, 29),
    (100, 541),
    (1_000, 7_919),
    (10_000, 104_729),
    (100_000, 1_299_709),
)


@pytest.mark.parametrize(("n", "truth_prime"), PRIME_CASES)
def test_nth_prime(n: int, truth_prime: int) -> None:
    assert nth_prime(n) == truth_prime


if __name__ == "__main__":
    print(f"Solution: {nth_prime()}")
