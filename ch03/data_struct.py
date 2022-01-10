""" data structures: tuple, list, dict, set """

T = (1, 2.5, 'data')
print(type(T))

T = 1, 2.5, 'data'
print(type(T))

print(T[2], type(T[2]))
print(T.count('data'), T.index(1))
