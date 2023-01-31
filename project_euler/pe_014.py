"""
Longest Collatz sequence
https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it
has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
from functools import cache


@cache
def collatz_length(val: int) -> int:
    # It's assumed but not proven that all Collatz sequences will terminate at 1
    if val == 1:
        return 1

    if val % 2 == 0:
        val //= 2
    else:
        val = 3 * val + 1

    # The length at each step is 1 more than the next step in
    # e.g. if we have CL(4): 4 -> 2 -> 1, its length is 3, which is 1 more than CL(2): 2 -> 1
    return collatz_length(val) + 1


def longest_collatz(limit: int = 1_000_000) -> int:  # pragma: no cover
    return max(range(1, limit), key=collatz_length)


def test_collatz_length() -> None:
    assert collatz_length(13) == 10


if __name__ == "__main__":
    print(f"Solution: {longest_collatz()}")
