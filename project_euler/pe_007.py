"""
10001st prime
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""
from helpers.matlib import estimate_prime, sieve_of_eratosthenes


def nth_prime(n: int = 10_001) -> int:
    u_bound = estimate_prime(n)
    sieved = sieve_of_eratosthenes(u_bound)
    for _ in range(n):
        nth = next(sieved)

    return nth


if __name__ == "__main__":
    print(f"Solution: {nth_prime()}")
