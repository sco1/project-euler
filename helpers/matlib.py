import math
import typing as t


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
