"""
Summation of primes
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from helpers.matlib import sieve_of_eratosthenes


def prime_summation(limit: int = 2_000_000) -> int:
    return sum(sieve_of_eratosthenes(limit))


def test_prime_summation() -> None:
    assert prime_summation(10) == 17


if __name__ == "__main__":
    print(f"Solution: {prime_summation()}")
