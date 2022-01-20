""" regular numpy array """
from pprint import pprint
import math
from timeit import timeit
import random
import time
import sys
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

# metainformation
print('G.size:', G.size)            # number of elements
print('G.itemsize:', G.itemsize)    # number of bytes to represent one element
print('G.ndim:', G.ndim)            # number of dimensions
print('G.shape:', G.shape)          # shape of the ndarray object
print('G.dtype:', G.dtype)          # data type of the elements
print('G.nbytes:', G.nbytes)        # total number of bytes used in memory

G = np.arange(15)
print('G:', G)
print('G.shape:', G.shape)
print('np shape G:', np.shape(G))
print('reshape:', G.reshape((3, 5)))

H = G.reshape((5, 3))
print('H:', H)
print('H.T:', H.T)
print('H.transpose():', H.transpose())

print('np resize G:', np.resize(G, (3, 1)))
print('np resize G:', np.resize(G, (1, 5)))
print('np resize G:', np.resize(G, (2, 5)))
print('np resize G:', np.resize(G, (5, 4)))

print('np hstack H:', np.hstack((H, 2*H)))
print('np vstack H:', np.vstack((H, 0.5*H)))

# default order for flattening is C
print('H flatten():', H.flatten())
print('H flatten(order C):', H.flatten(order='C'))
# flattening with F order
print('H flatten(order F):', H.flatten(order='F'))

for i in H.flat:
    print(i, end=',')
print()

# ravel() method is an alternative to flatten()
for i in H.ravel(order='C'):
    print(i, end=',')
print()

for i in H.ravel(order='F'):
    print(i, end=',')
print()

print('H:', H)
print('H > 8:', H > 8)
print('H <= 7:', H <= 7)
print('H == 5:', H == 5)
print('(H == 5).astype(int):', (H == 5).astype(int))
print('(H > 4) & (H <= 12):', (H > 4) & (H <= 12))

print('H[H > 8]:', H[H > 8])
print('H[(H > 4) & (H <= 12)]:', H[(H > 4) & (H <= 12)])
print('H[(H < 4) | (H >= 12)]:', H[(H < 4) | (H >= 12)])

# set 1 if True and 0 otherwise
print('np where:', np.where(H > 7, 1, 0))
print('np where:', np.where(H % 2 == 0, 'even', 'odd'))
print('np where:', np.where(H <= 7, H * 2, H / 2))

DIM = 5000
T1 = time.time()
mat = [[random.gauss(0, 1) for j in range(DIM)]
       for i in range(DIM)]
T2 = time.time()
print('time to create matrix:', T2 - T1)
print('mat[0][:5]:', mat[0][:5])

T1 = time.time()
SUM = sum([sum(llist) for llist in mat])
T2 = time.time()
print('time to find sum of matrix:', T2 - T1)
print('sum of matrix:', SUM)
SUM = sum([sys.getsizeof(llist) for llist in mat])
print('total memory usage of matrix:', SUM)

T1 = time.time()
mat = np.random.standard_normal((DIM, DIM))
T2 = time.time()
print('time to create matrix:', T2 - T1)

T1 = time.time()
SUM = mat.sum()
T2 = time.time()
print('time to find sum of matrix:', T2 - T1)
print('sum of matrix:', SUM)
print('mat nbytes:', mat.nbytes)
print('total memory usage of matrix:', sys.getsizeof(mat))
