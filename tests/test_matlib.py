import pytest

from helpers.matlib import estimate_prime, triangle_numbers

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
