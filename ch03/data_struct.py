""" data structures: tuple, list, dict, set """
from random import randint

T = (1, 2.5, 'data')
print(type(T))

T = 1, 2.5, 'data'
print(type(T))

print(T[2], type(T[2]))
print(T.count('data'), T.index(1))

L = [1, 2.5, 'data']
print(L[2])

L = list(T)
print(L, type(L))

L.append([4, 3])
print(L)

L.extend([1.0, 1.5, 2.0])
print(L)

L.insert(1, 'insert')
print(L)

L.remove('data')
print(L)

P = L.pop(3)
print(L, P)

print('L[2:5]:', L[2:5])

R = range(0, 8, 1)
print(R, type(R))

for i in range(1, 10):
  if i % 2 == 0:
    print(f'{i:d} is even')
  elif i % 3 == 0:
    print(f'{i:d} is multiple of 3')
  else:
    print(f'{i:d} is odd')

M = [i ** 2 for i in range(5)]
print(M)

def isEven(x):
  return x % 2 == 0
result = list(map(isEven, range(10)))
print(result)

result = list(map(lambda x: x ** 2, range(10)))
print(result)

result = list(filter(isEven, range(15)))
print(result)

D = {'Name': 'Angela Merkel',
     'Country': 'Germany',
     'Profession': 'Chancelor',
     'Age': 64}
print(D, type(D))
print(D['Name'], D['Age'])
print(D.keys())
print(D.values())
print(D.items())

BIRTHDAY = True
if BIRTHDAY:
  D['Age'] += 1
print(D['Age'])

S = set(['u', 'd', 'ud', 'du', 'd', 'du'])
print('S:', S)

T = set(['d', 'dd', 'uu', 'u'])
print('T:', T)
print('S union T:', S.union(T))
print('S intersection T:', S.intersection(T))
print('S difference T', S.difference(T))
print('T difference S', T.difference(S))
# items in either S or T but not both
print('S symmetric difference T:', S.symmetric_difference(T))

L = [randint(0, 10) for i in range(1000)]
print('L length:', len(L))
print(L[:20])
S = set(L)
print(S)