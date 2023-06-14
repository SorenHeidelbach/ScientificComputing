"""
Dirty example of unittest and doctest

Can be run as python doc_test.py


"""

import doctest

import find_primes

doctest.testmod(find_primes, verbose=True)

import exercise1

doctest.testmod(exercise1, verbose=True)


