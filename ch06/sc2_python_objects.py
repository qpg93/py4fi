""" python objects """
import numpy as np
import pandas as pd


# int
N = 5
print('type N:\n', type(N))
print('N numerator:\n', N.numerator)
print('N bit length:\n', N.bit_length())
print('N + N:\n', N + N)
print('2 * N:\n', 2 * N)
# memory usage (special method)
print('size of N:\n', N.__sizeof__())

# list
L = [1, 2, 3, 4]
print('type L:\n', type(L))
print('L[0]:\n', L[0])
L.append(10)
print('L after appending 10:\n', L)
print('L + L:\n', L + L)
print('2 * L:\n', 2 * L)
print('sum L:\n', sum(L))
print('size of L:\n', L.__sizeof__())

# ndarray
A = np.arange(16).reshape((4, 4))
print('A:\n', A)
print('type A:\n', type(A))
print('A nbytes:\n', A.nbytes)
print('A sum:\n', A.sum())
print('A cumsum axis=0:\n', A.cumsum(axis=0))
print('A + A:\n', A + A)
print('2 * A:\n', 2 * A)
print('sum A:\n', sum(A))
print('np sum A:\n', np.sum(A))
print('size of A:\n', A.__sizeof__())

# dataframe
df = pd.DataFrame(A, columns=list('abcd'))
print('df:\n', df)
print('type df:\n', type(df))
print('df columns:\n', df.columns)
print('df sum:\n', df.sum())
print('df cumsum:\n', df.cumsum())
print('df + df:\n', df + df)
print('2 * df:\n', 2 * df)
print('np sum df:\n', np.sum(df))
print('size of df:\n', df.__sizeof__())
