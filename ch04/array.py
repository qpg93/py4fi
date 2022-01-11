from pprint import pprint
from copy import deepcopy
import array

V = [0.5, 0.75, 1.0, 1.5, 2.0]
M = [V, V, V]
pprint(M)

V1 = [0.5, 1.5]
V2 = [1, 2]
M = [V1, V2]
C = [M, M]
pprint(C)
print('C[1][1][0]:', C[1][1][0])

M = [V, V, V]
V[0] = 'Python'
pprint(M)

V = [0.5, 0.75, 1.0, 1.5, 2.0]
M = 3 * [deepcopy(V)]
V[0] = 'Python'
pprint(M)

V = [0.5, 0.75, 1.0, 1.5, 2.0]
# instantiation of array object with float as type code
A = array.array('f', V)
print('A:', A)

A.append(0.5)
print('A append:', A)

A.extend([5.0, 6.75])
print('A extend:', A)

print('2 * A:', 2 * A)

# only float objects can be appended, other data types raise errors
# A.append('string')
# TypeError: must be real number, not str

print('A tolist:', A.tolist())

with open('array.apy', 'wb') as fileport:
  A.tofile(fileport)

B = array.array('f')
with open('array.apy', 'rb') as fileport:
  # read 5 elements in object
  B.fromfile(fileport, 5)
print('B:', B)

B = array.array('d')
with open('array.apy', 'rb') as fileport:
  # read 2 elements in object
  B.fromfile(fileport, 2)
# the difference in type codes leads to "wrong" numbers
print('B:', B)