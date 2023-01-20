from project_euler.pe_008 import largest_adjacent_prod


def test_largest_adjacent_prod() -> None:
    assert largest_adjacent_prod(n=4) == 5832
