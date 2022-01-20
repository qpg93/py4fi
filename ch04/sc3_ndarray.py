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
