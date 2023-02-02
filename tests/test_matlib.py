import pytest

from helpers.matlib import estimate_prime, fibonacci, n_digits, proper_divisors, triangle_numbers

PRIME_ESTIMATE_CASES = (
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


@pytest.mark.parametrize(("n", "nth_prime"), PRIME_ESTIMATE_CASES)
def test_prime_estimation(n: int, nth_prime: int) -> None:
    assert nth_prime <= estimate_prime(n)


def test_triangle_numbers() -> None:
    nums = triangle_numbers()
    assert [next(nums) for _ in range(7)] == [1, 3, 6, 10, 15, 21, 28]


def test_proper_divisors() -> None:
    assert proper_divisors(220) == {1, 2, 4, 5, 10, 11, 44, 110, 20, 22, 55}


def test_fibonacci() -> None:
    fib = fibonacci()
    assert [next(fib) for _ in range(12)] == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]


DIGITS_CASES = (
    (1, 1),
    (10, 2),
    (100, 3),
    (10_000_000, 8),
)


@pytest.mark.parametrize(("n", "truth_count"), DIGITS_CASES)
def test_n_digits(n: int, truth_count: int) -> None:
    assert n_digits(n) == truth_count
