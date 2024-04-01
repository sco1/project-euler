"""
Lattice paths
https://projecteuler.net/problem=15

Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

import math


def n_lattice_paths(grid_size: int = 20) -> int:
    # We have grid_size total x values and grid_size total y values to choose from
    # Since we can only move right or down, we have to move exactly grid_size times in order to get
    # to the bottom right corner
    # AKA biomial coefficient (n choose k)
    return math.comb(2 * grid_size, grid_size)


def test_n_lattice_paths() -> None:
    assert n_lattice_paths(2) == 6


if __name__ == "__main__":
    print(f"Solution: {n_lattice_paths()}")
