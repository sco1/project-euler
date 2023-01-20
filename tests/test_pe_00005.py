import pytest

from project_euler.pe_00005 import lowest_common_multiple

LCM_CASES = (
    (3, 6),
    (5, 60),
    (7, 420),
    (10, 2520),
)


@pytest.mark.parametrize(("n", "truth_lcm"), LCM_CASES)
def test_lowest_common_multiple(n: int, truth_lcm: int) -> None:
    assert lowest_common_multiple(n) == truth_lcm
