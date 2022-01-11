from pprint import pprint
import numpy as np
import math
from timeit import timeit

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