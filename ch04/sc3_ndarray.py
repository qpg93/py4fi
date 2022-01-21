""" structured ndarray & vectorization of code """
from timeit import timeit
import numpy as np

# structured ndarray
# complex dtype composition
dt = np.dtype([('Name', 'S10'), ('Age', 'i4'),
               ('Height', 'f'), ('Children/Pets', 'i4', 2)])
print('dt:', dt)

dt = np.dtype({'names': ['Name', 'Age', 'Height', 'Children/Pets'],
               'formats': 'O int float int,int'.split()})
print('dt:', dt)

S = np.array([('Smith', 45, 1.83, (0, 1)),
              ('Jones', 53, 1.72, (2, 2))], dtype=dt)

print('S:', S)
print('S type:', type(S))
# column selection by name
print("S['Name']:", S['Name'])
# column method calling
print("S['Height'] mean:", S['Height'].mean())
# record(line) selection
print('S[0]:', S[0])
# field selection in a record(line)
print("S[1]['Age']:", S[1]['Age'])

# basic vectorization
np.random.seed(100)
R = np.arange(12).reshape((4, 3))
S = np.arange(12).reshape((4, 3)) * 0.5
print('R:', R)
print('S:', S)
# element-wise addition
print('R + S:', R + S)
# scalar is broadcast and added to every element
print('R + 3:', R + 3)
# scalar is broadcast and multiplied to every element
print('2 * R:', 2 * R)
print('2 * R + 3:', 2 * R + 3)

print('R shape:', R.shape)
S = np.arange(0, 12, 4)
print('S:', S)
print('R + S:', R + S)

S = np.arange(0, 12, 3)
print('S:', S)
# ValueError: operands could not be broadcast together with different shapes
# print('R + S:', R + S)

# transposing R again allows for vectorized addition
print('R.transpose() + S:', R.transpose() + S)

SR = S.reshape(-1, 1)
print('SR:', SR)
print('SR shape:', SR.shape)
print('R + S.reshape:', R + S.reshape(-1, 1))


def calc(num):
    """ calculate y=3x+5 """
    return 3 * num + 5


print('calc(0.5):', calc(0.5))
# function applied to ndarray object (vectorized & element-wise)
print('calc(R):', calc(R))

# memory layout
X = np.random.standard_normal((1000000, 5))
Y = 2 * X + 3
# C order (row-major)
C = np.array((X, Y), order='C')
# F order (row-major)
F = np.array((X, Y), order='F')
# memory is freed up (contingent on garbage collection)
X, Y = 0., 0.
print('C[:2] round:', C[:2].round(2))

SETUP = r"""
import numpy as np
X = np.random.standard_normal((1000000, 5))
Y = 2 * X + 3
C = np.array((X, Y), order='C')
F = np.array((X, Y), order='F')
X, Y = 0., 0.
"""

T = timeit(stmt='C.sum()', setup=SETUP, number=100)
print('C sum time duration:', T)

T = timeit(stmt='F.sum()', setup=SETUP, number=100)
print('F sum time duration:', T)

# calculate sums per row ('many')
T = timeit(stmt='C.sum(axis=0)', setup=SETUP, number=10)
print('C sum axis=0 time duration:', T)

# calculate sums per column ('few')
T = timeit(stmt='C.sum(axis=1)', setup=SETUP, number=10)
print('C sum axis=1 time duration:', T)

T = timeit(stmt='F.sum(axis=0)', setup=SETUP, number=10)
print('F sum axis=0 time duration:', T)

T = timeit(stmt='F.sum(axis=1)', setup=SETUP, number=10)
print('F sum axis=1 time duration:', T)

F, C = 0., 0.
