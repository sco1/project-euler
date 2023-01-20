"""
Sum square difference
https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square
of the sum is 3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the
square of the sum.
"""


def sum_square_diff(n: int = 100) -> int:
    # Start from the already derived closed-form solutions to the sum of first n squares:
    # S_s2 = (n * (n + 1) * (2*n + 1)) / 6 = (n^3 / 3) + (n^2 / 2) + (n / 6)
    # And the square of the sum of the first n numbers:
    # S2 = ((n * (n + 1)) / 2)^2 = (n^4 / 4) + (n^3 / 3) + (n^2 / 4)
    #
    # Subtracting the two gives us:
    # S2 - S_s2 = (3*n^4 + 2*n^3 - 3*n^2 - 2*n)/12
    #
    # This should already always be an int but might have to be careful with this cast in a more
    # generic application
    return int((3 * n**4 + 2 * n**3 - 3 * n**2 - 2 * n) / 12)


def test_sum_square_diff() -> None:
    assert sum_square_diff(10) == 2640


if __name__ == "__main__":
    print(f"Solution: {sum_square_diff()}")
