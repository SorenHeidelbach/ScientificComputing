def add(a, b):
    r = a + b
    return r

A = [1, 2.0, 'add' , (1, 2, 3), (1, 2, 4)]
B = [2, 0.8, ' me' , (-1, 2)  , (3,)]
C = [3, 6.2, ' too', (4, 5, 6), (4)]

T = list(map(add, A, B))
R = list(map(add, T, C))
