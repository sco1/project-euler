"""
1000-digit Fibonacci number
https://projecteuler.net/problem=25

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

from helpers.matlib import fibonacci


def first_n_digit_fib_idx(n: int = 1000) -> int:
    for idx, val in enumerate(fibonacci(), start=1):
        # Could do powers but strings are lazier
        if len(str(val)) >= n:
            return idx

    raise ValueError("Surprise! You can't get here.")  # pragma: no cover


def test_first_n_digit_fib_idx() -> None:
    assert first_n_digit_fib_idx(3) == 12


if __name__ == "__main__":
    print(f"Solution: {first_n_digit_fib_idx()}")
