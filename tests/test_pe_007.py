import pytest

from project_euler.pe_007 import nth_prime

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
