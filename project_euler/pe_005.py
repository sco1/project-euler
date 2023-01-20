"""
Smallest multiple
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any
remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import math


def lowest_common_multiple(n: int = 20) -> int:
    # Info from: https://mathworld.wolfram.com/LeastCommonMultiple.html
    # LCM(a,b) is calculated as (a*b)/GCD(a, b)
    # Or, LCM(a, b, c) = LCM(a, LCM(b, c))
    # So, LCM(a, b, c) = a * (b/GCD(a, b)) * (c/GCD(b, c))
    lcm = 1
    for i in range(1, n + 1):
        # I guess I should implement my own GCD but I'll half cheat
        lcm *= i // math.gcd(lcm, i)

    return lcm


if __name__ == "__main__":
    print(f"Solution: {lowest_common_multiple()}")
