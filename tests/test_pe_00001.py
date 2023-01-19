from project_euler.pe_00001 import multiples_sum, multiples_sum_brute


def test_multiples_sum() -> None:
    assert multiples_sum(cap=10) == 23


def test_multiples_sum_brute() -> None:
    assert multiples_sum_brute(cap=10) == 23
