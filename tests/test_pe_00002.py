from project_euler.pe_00002 import sum_even_fib


def test_even_fib() -> None:
    assert sum_even_fib(cap=100) == 44
