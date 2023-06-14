"""
Can be run as `pytest` in current folder

or

$ python -m pytest

"""

import pytest
from find_primes import primes

from exercise1 import midpointintegration


class TestPrimes:
    
    def test_boundary(self):
        assert primes(0) == []
        assert primes(1) == []
        assert primes(2) == [2]
        
    def test_case(self):
        assert primes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


class TestMidpointIntegration:
    def test_case(self):
        assert midpointintegration(lambda x: x**2, 1, 2, 2) == 0.78125
        assert midpointintegration(lambda x: x**2, 1, 1, 2) == 0.0
    def test_negative_inetragetion(self):
        assert midpointintegration(lambda x: x**2, -1, 2, 2) == 0.09375
    def test_type_error(self):
        with pytest.raises(TypeError):
            midpointintegration(lambda x: x**2, 'a', 2, 2)
        with pytest.raises(TypeError):
            midpointintegration(lambda x: x**2, '2', "2", "2")