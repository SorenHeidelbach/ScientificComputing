"""
Sorts the data according to an index

"""

import sys

def sorted_index(data, index=0):
    """
    Sorts the data (ascending) according to index, i.e.

     data[i][index] > data[j][index], for all i > j

    INPUT::

     data: to sort
     index: default index=1

    OUPUT::

      data: sorted data
    
    Examples

    >>> data = [(1, 'a', 6), (2, 'b', 8), (10, 'c', 1)]
    >>> sorted_index(data)
    [(1, 'a', 6), (2, 'b', 8), (10, 'c', 1)]
    >>> sorted_index(data, 2)
    [(10, 'c', 1), (1, 'a', 6), (2, 'b', 8)]

    """

    # This only works on python 2.x (cmp keyword argument is removed in 3.x)
    # def my_sort(a, b):
    #    return cmp(a[key], b[key])
    #
    #return sorted(data, key=2)

    # This works for both python 2.x and python 3.x
    def fkey(e):
        return e[index]

    return sorted(data, key=fkey)

def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()

        
