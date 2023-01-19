import pytest

from project_euler.pe_00003 import largest_prime_factor

LPF_CASES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 2),
    (128, 2),
    (126, 7),
    (13_195, 29),
)


@pytest.mark.parametrize(("val", "truth_lpf"), LPF_CASES)
def test_largest_prime_factor(val: int, truth_lpf: int) -> None:
    assert largest_prime_factor(val) == truth_lpf
