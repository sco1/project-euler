"""
Power digit sum
https://projecteuler.net/problem=16

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""


def digit_sum_python_abuse(power: int = 1000) -> int:
    """
    Calculate the sum of the digits of `2` to the specified `power`.

    The cheating way, using Python's arbitrary integer support
    """
    return sum(int(c) for c in str(2**power))


def test_digit_sum_python_abuse() -> None:
    assert digit_sum_python_abuse(15) == 26


if __name__ == "__main__":
    print(f"Cheating Solution: {digit_sum_python_abuse()}")
