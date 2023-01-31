"""
Maximum path sum I
https://projecteuler.net/problem=18

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the
maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below.

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be
solved by brute force, and requires a clever method! ;o)
"""

PUZZLE_TRIANGLE = """\
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


def parse_tree(raw: str) -> list[list[int]]:
    rows = []
    for line in raw.splitlines():
        rows.append([int(chunk) for chunk in line.strip().split()])

    return rows


def find_max_path_sum(tree: list[list[int]]) -> int:
    """Find the maximum total from top to bottom of the provided tree, assumed to be a pyramid."""
    # Rather than brute forcing from top-down, start from the bottom & work up using tiny baby
    # pyramids and calculating the maximal path along the way.
    # e.g. for the sample triangle, start with the 2-8-5, 4-5-9, 6-9-3 triangles and work up
    n_rows = len(tree)
    for y in range(n_rows - 2, -1, -1):  # Start from second to last row to the 0th row
        for x in range(len(tree[y])):
            tree[y][x] += max(tree[y + 1][x], tree[y + 1][x + 1])

    # Once we get to the top, we should have found our maximum path?
    return tree[0][0]


# Made pyramid-like to help my brain, parsed tree should end up the same
SAMPLE_TRIANGLE = """\
   3
  7 4
 2 4 6
8 5 9 3
"""


def test_find_max_path_sum() -> None:
    assert find_max_path_sum(parse_tree(SAMPLE_TRIANGLE)) == 23


if __name__ == "__main__":
    print(f"Solution: {find_max_path_sum(parse_tree(PUZZLE_TRIANGLE))}")
