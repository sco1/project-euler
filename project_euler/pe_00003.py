"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


def largest_prime_factor(num: int = 600_851_475_143) -> int:  # noqa: D103
    if num in range(1, 4):  # Short-circuit on the easy ones
        return num

    # The ordinary factorization tree seems speedy enough
    largest_factor = -1
    while num > 1:
        for i in range(2, num + 1):
            if num % i == 0:
                largest_factor = max(largest_factor, i)
                num //= i
                break

    return largest_factor


if __name__ == "__main__":
    print(f"Solution: {largest_prime_factor()}")
