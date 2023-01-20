"""
Multiples of 3 or 5
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The
sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multiples_sum_brute(a: int = 3, b: int = 5, cap: int = 1000) -> int:
    """Find the sum of all natural numbers below `cap` that are multiples of `a` or `b`."""
    return sum(val for val in range(cap) if (val % a == 0 or val % b == 0))


def simp_arith_series(divisor: int, cap: int) -> int:
    """
    Calculate the sum of a finite arithmetic progression with the given parameters.

    See: https://en.wikipedia.org/wiki/Arithmetic_progression
    """
    # We can rewrite the series of divisible values as n*(1, 2, ..., (cap-1)/n)
    # e.g. (3, 6, ..., 999) -> 3*(1, 2, ..., 333) and (5, 10, ..., 995) -> 5*(1, 2, ..., 199)
    # We can floor div without worrying about info loss because the sum of 2 numbers is always even
    n = (cap - 1) // divisor
    return divisor * ((n * (1 + n)) // 2)


def multiples_sum(a: int = 3, b: int = 5, cap: int = 1000) -> int:
    """Find the sum of all natural numbers below `cap` that are multiples of `a` or `b`."""
    a_sum = simp_arith_series(a, cap)
    b_sum = simp_arith_series(b, cap)

    # Summing these 2 series will double count multiples of the product, so we can use the
    # inclusion-exclusion principle to eliminate their contribution
    ab = a * b
    ab_sum = simp_arith_series(ab, cap)

    return a_sum + b_sum - ab_sum


def test_multiples_sum() -> None:
    assert multiples_sum(cap=10) == 23


def test_multiples_sum_brute() -> None:
    assert multiples_sum_brute(cap=10) == 23


if __name__ == "__main__":
    print(f"Solution: {multiples_sum()}")
