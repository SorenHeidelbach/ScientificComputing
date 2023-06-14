"""
Accelerated sorting and selection functions using Numba.

"""

from numba import jit
import numpy as np

@jit
def selection(a, K):
    """
    Returns the value and index of the :math:`K`th largest element in the numpy
    array `a`.

    INPUT::

     a:     Numpy array
     K:     int

    OUTPUT::

     s:     The Kth largest value (1 <= K <= N; N length of a)
     i:     Index of the Kth largest value. If the index is not unique
            returns the first index such that s=a[i].

    Implements selection from Press et al., Numerical Recipes, 3rd Ed.,
    Cambridge University Press, 2007.

    Example:

    >>> a = np.asarray([10., 7., 6., 5., 4., 3., 2., 1.])
    >>> selection(a, 1)
    (10.0, 0)
    >>> selection(a, 4)
    (5.0, 3)

    """

    N = len(a)
    K = N - K  # Make algorithm find largest instead of smallest entry

    # The function performs inplace operations
    ak = a.copy()

    idx_l = 0
    idx_ir = N - 1
    while True:  # Loop ended by return statement inside
        if idx_ir <= (idx_l + 1):
            if idx_ir == (idx_l + 1) and ak[idx_ir] < ak[idx_l]:
                ak[idx_l], ak[idx_ir] = ak[idx_ir], ak[idx_l]
            return ak[K], np.where(ak[K] == a)[0][0]
        else:
            mid = int((idx_l + idx_ir) / 2)
            ak[mid], ak[idx_l + 1] = ak[idx_l + 1], ak[mid]
            if ak[idx_l] > ak[idx_ir]:
                ak[idx_l], ak[idx_ir] = ak[idx_ir], ak[idx_l]
            if ak[idx_l + 1] > ak[idx_ir]:
                ak[idx_l + 1], ak[idx_ir] = ak[idx_ir], ak[idx_l + 1]
            if ak[idx_l] > ak[idx_l + 1]:
                ak[idx_l], ak[idx_l + 1] = ak[idx_l + 1], ak[idx_l]
            idx_i = idx_l + 1
            idx_j = idx_ir
            elem_a = ak[idx_l + 1]
            while True:
                idx_i += 1  # Emulate do-while from Press et al.
                while ak[idx_i] < elem_a:
                    idx_i += 1
                idx_j -= 1  # Emulate do-while from Press et al.
                while ak[idx_j] > elem_a:
                    idx_j -= 1
                if idx_j < idx_i:
                    break
                ak[idx_i], ak[idx_j] = ak[idx_j], ak[idx_i]
            ak[idx_l + 1] = ak[idx_j]
            ak[idx_j] = elem_a
            if idx_j >= K:
                idx_ir = idx_j - 1
            if idx_j <= K:
                idx_l = idx_i


@jit
def _sift_down(a, idx_l, idx_r):
    """
    Utility function for `heap_sort`.

    """

    elem_a = a[idx_l]
    idx_j_old = idx_l
    idx_j = 2 * idx_l + 1
    while idx_j <= idx_r:
        if (idx_j < idx_r and a[idx_j] < a[idx_j + 1]):
            idx_j += 1
        if elem_a >= a[idx_j]:
            break
        a[idx_j_old] = a[idx_j]
        idx_j_old = idx_j
        idx_j = 2 * idx_j + 1
    a[idx_j_old] = elem_a
    # No need to return anything, the result is in a


@jit
def heap_sort(a):
    """
    Returns a sorted numpy array (ascending)

    INPUT::

     a:     Numpy array

    OUTPUT::

     ak:    Sorted Numpy array

    Implements heap sort from Press et al., Numerical Recipes, 3rd Ed.,
    Cambridge University Press, 2007.

    >>> a = np.asarray([10., 7., 6., 5., 4., 3., 2., 1.])
    >>> np.all(heap_sort(a) == np.asarray([1., 2., 3., 4., 5., 6., 7., 10.]))
    True

    """

    N = len(a)

    # The function performs inplace operations
    ak = a.copy()

    for idx in range(int(N / 2 - 1), 0 - 1, -1):
        _sift_down(ak, idx, N - 1)
    for idx in range(N - 1, 0, -1):
        ak[0], ak[idx] = ak[idx], ak[0]
        _sift_down(ak, 0, idx - 1)
    return ak


def _test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    _test()
