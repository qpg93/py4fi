""" performance aspects """
import time
import numpy as np
import pandas as pd

np.random.seed(1)

data = np.random.standard_normal((1000000, 2))
print('data nbytes:\n', data.nbytes)

df = pd.DataFrame(data, columns=['x', 'y'])
print('data info:\n', df.info())

T1 = time.time()
res = df['x'] + df['y']
T2 = time.time()
print('time +:\n', T2 - T1)
# print('res[:3]:\n', res[:3])

T1 = time.time()
res = df.sum(axis=1)
T2 = time.time()
print('time df sum:\n', T2 - T1)
# print('res[:3]:\n', res[:3])

T1 = time.time()
res = df.values.sum(axis=1)
T2 = time.time()
print('time df values sum:\n', T2 - T1)
# print('res[:3]:\n', res[:3])

T1 = time.time()
res = np.sum(df, axis=1)
T2 = time.time()
print('time np sum:\n', T2 - T1)
# print('res[:3]:\n', res[:3])

T1 = time.time()
res = df.eval('x + y')
T2 = time.time()
print('time df eval +:\n', T2 - T1)
# print('res[:3]:\n', res[:3])

T1 = time.time()
res = df.apply(lambda row: row['x'] + row['y'], axis=1)
T2 = time.time()
print('time df apply lambda:\n', T2 - T1)
# print('res[:3]:\n', res[:3])
