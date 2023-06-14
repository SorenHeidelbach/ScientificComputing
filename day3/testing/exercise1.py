
"""
Exercise 1 of scientific computing
"""

def midpointintegration(f, a, b, n):
    """

    Finds the midpoint integration of a function f between a and b with n steps
    example
    >>> midpointintegration(lambda x: x**2, 1, 2, 2)
    0.78125
    >>> midpointintegration(lambda x: x**3, 1, 2, 2)
    0.9765625
    """
    sum = 0
    h = (b-a)/n
    for i in range (n-1):
        x = (a + 0.5 * h + i * h)
        sum += h * f(x)
    return sum




