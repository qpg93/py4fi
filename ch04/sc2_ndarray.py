""" numpy array """
from pprint import pprint
import math
from timeit import timeit
import numpy as np

# basics
A = np.array([0, 0.5, 1.0, 1.5, 2.0])
pprint(A)

A = np.array(['a', 'b', 'c'])
pprint(A)

A = np.arange(2, 20, 2)
pprint(A)

A = np.arange(8, dtype=np.float64)
pprint(A)

pprint(A[5:])
pprint(A[:2])

print('A sum:', A.sum())
print('A std:', A.std())
# cumulative sum of all elements
# (starting at index position 0)
print('A cumsum:', A.cumsum())

L = [0., 0.5, 1.5, 3., 5.]
print('L:', L)
print('2 * L:', 2 * L)

print()
print('A:', A)
print('2 * A:', 2 * A)
print('A ** 2:', A ** 2)
print('2 ** A:', 2 ** A)
print('A ** A:', A ** A)

print('np exp A:', np.exp(A))
print('np sqrt A:', np.sqrt(A))
print('np sqrt 2.5:', np.sqrt(2.5))
print('math sqrt 2.5', math.sqrt(2.5))

# math.sqrt(A)
# TypeError: only size-1 arrays can be converted to Python scalars

T1 = timeit(stmt='np.sqrt(2.5)',
            setup='import numpy as np',
            number=1000000)
T2 = timeit(stmt='math.sqrt(2.5)',
            setup='import math',
            number=1000000)
print('Timeit np sqrt:', T1)
print('Timeit math sqrt:', T2)

# multiple dimensions
B = np.array([A, A * 2])
pprint(B)

print('B[0]:', B[0])
print('B[0, 2]:', B[0, 2])
print('B[:, 1]:', B[0])
print('B sum:', B.sum())
print('B sum axis=0:', B.sum(axis=0))
print('B sum axis=1:', B.sum(axis=1))

C = np.zeros((2, 3), dtype='i', order='C')
pprint(C)

C = np.ones((2, 3, 4), dtype='i', order='C')
pprint(C)

D = np.zeros_like(C, dtype='f16', order='C')
pprint(D)

D = np.ones_like(C, dtype='f16', order='C')
pprint(D)

# array not prepopulated with anything
# numbers depend on the bits present in the memory
E = np.empty((2, 3, 2))
pprint(E)

F = np.empty_like(C)
pprint(F)

# diagonal populated by 1
G = np.eye(5)
pprint(G)

# one-dimensional array evenly spaced intervals between numbers
# parameters: start, end, number of elements
G = np.linspace(5, 15, 12)
pprint(G)
