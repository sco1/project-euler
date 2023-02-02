import itertools
import math
import typing as t
from functools import lru_cache


def estimate_prime(n: int) -> int:
    """
    Use the prime number theorem to estimate the upper boundary of the nth prime.

    See: https://en.wikipedia.org/wiki/Prime_number_theorem
    See: https://mathscinet.ams.org/mathscinet-getitem?mr=1406794
    """
    # From the provided textbook source, the upper bound estimate is valid for n>=6, so we can just
    # hardcode the boundary for the first 6 primes to an arbitrary number. The search space for n
    # this small is also very small
    if n <= 6:
        return 14

    estimated = math.ceil(n * math.log(n) + n * math.log(math.log(n)))
    return estimated


def sieve_of_eratosthenes(limit: int) -> t.Generator[int, None, None]:
    """
    Yield all prime numbers below the specified limit.

    Derived from: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    if limit <= 1:
        return None

    mark = [True] * limit
    mark[0] = mark[1] = False
    for idx, marked_prime in enumerate(mark):
        if marked_prime:
            yield idx

            # Strike off multiples of the current prime by incrementing until we hit the upper limit
            # Includes the optimization where we start at the square of the current prime and
            # increment from there
            for k in range(idx**2, limit, idx):
                mark[k] = False


def gcd(a: int, b: int) -> int:  # noqa: D103
    # See: https://en.wikipedia.org/wiki/Euclidean_algorithm
    while b != 0:
        a, b = b, a % b

    return a


def is_coprime(a: int, b: int) -> bool:  # noqa: D103
    return math.gcd(a, b) == 1


def triangle_numbers() -> t.Generator[int, None, None]:  # noqa: D103
    num = 0
    for i in itertools.count(1):  # pragma: no branch
        num += i
        yield num


@lru_cache()
def proper_divisors(n: int) -> set[int]:  # noqa: D103
    divisors = {1}
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)

    return divisors


def fibonacci() -> t.Generator[int, None, None]:  # noqa: D103
    n_2 = n_1 = 1
    yield n_2
    yield n_1

    while True:
        n_2, n_1 = n_1, (n_2 + n_1)
        yield n_1


def n_digits(n: int) -> int:  # noqa: D103
    return math.floor(math.log10(n)) + 1
