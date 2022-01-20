""" structured ndarray & vectorization of code """
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
