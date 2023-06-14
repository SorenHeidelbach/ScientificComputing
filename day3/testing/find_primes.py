
"""
Find all the primes up to n using the algorithm:

   Sieve of Eratosthenes

"""


def primes(n):
    """
    Computes all the primes up to and including n using the algorithm

       Sieve of Eratosthenes

    (INPUT)
    n: integer

    (OUTPUT)
    returns a list of primes

    Example usage:
    >>> primes(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> primes(1)
    []

    """

    a = [False]*2 + [True]*(n-1)  # this gives simple indexing

    for k in range(2, n+1):  # can be improved by only going to sqrt(n)

        if a[k]:
            for p in range(2*k, n+1, k):
                a[p] = False

    return [i for i, x in enumerate(a) if x is True]


