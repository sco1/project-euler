"""
Number letter counts
https://projecteuler.net/problem=17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many
letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23
letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out
numbers is in compliance with British usage.
"""

import pytest

BASE_COUNTS = {
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6,
}

SUPPORTED_LIMIT = 10_000


def number_letter_count(n: int) -> int:
    """
    Count the number of letters used to express `n`.

    NOTE: Spaces or hyphens are not counted. "and"s are counted.
    """
    if n >= SUPPORTED_LIMIT:
        raise ValueError(f"Values <={SUPPORTED_LIMIT:,} are not supported")

    # Since we know what our problem bounds are, we can manually split our number into its lowest
    # complexity components, e.g. we want to consider 11,125 as 11, 1, 20, and 5
    # This seemed like an interesting approach but doesn't appear scale very well, at least how I've
    # written it :D
    letter_count = 0
    component_queue = [n]
    while component_queue:
        val = component_queue.pop()
        if val in BASE_COUNTS:
            letter_count += BASE_COUNTS[val]
        elif 20 < val < 100:
            tens, rem = divmod(val, 10)
            letter_count += BASE_COUNTS.get(tens * 10, 0) + BASE_COUNTS[rem]
        elif 100 <= val < 1_000:
            hundreds, rem = divmod(val, 100)
            letter_count += BASE_COUNTS.get(hundreds, 0) + len("hundred")
            if rem:
                letter_count += len("and")
                component_queue.append(rem)
        elif 1_000 <= val < 10_000:  # pragma: no branch
            thousands, rem = divmod(val, 1000)
            component_queue.append(thousands)
            letter_count += len("thousand")
            if rem:
                component_queue.append(rem)
                if rem < 100:  # pragma: no branch
                    letter_count += len("and")

    return letter_count


def total_letter_count(limit: int = 1000) -> int:
    """
    Count the number of letters used to express the numbers from `1` to `limit`, inclusive.

    NOTE: Spaces or hyphens are not counted. "and"s are counted.
    """
    if limit >= SUPPORTED_LIMIT:
        raise ValueError(f"Values <={SUPPORTED_LIMIT:,} are not supported")

    return sum((number_letter_count(n) for n in range(1, limit + 1)))


LETTER_COUNT_TEST_CASES = (
    (1, 3),
    (12, 6),
    (23, 11),
    (100, 10),
    (101, 16),
    (115, 20),
    (342, 23),
    (1_000, 11),
    (1_001, 17),
)


def test_large_number_raises() -> None:
    with pytest.raises(ValueError):
        number_letter_count(SUPPORTED_LIMIT)


@pytest.mark.parametrize(("n", "truth_count"), LETTER_COUNT_TEST_CASES)
def test_number_letter_count(n: int, truth_count: int) -> None:
    assert number_letter_count(n) == truth_count


def test_large_limit_raises() -> None:
    with pytest.raises(ValueError):
        total_letter_count(SUPPORTED_LIMIT)


def test_total_letter_count() -> None:
    assert total_letter_count(5) == 19


if __name__ == "__main__":
    print(f"Solution: {total_letter_count()}")
