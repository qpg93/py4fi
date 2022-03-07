""" basic i/o with python """
import pickle
import csv
import datetime
from random import gauss
from pylab import plt, mpl
import numpy as np
import pandas as pd
import sqlite3 as sq3
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

# writing objects to disk
A = [gauss(1.5, 2) for i in range(1000000)]
PATH = './'
with open(PATH+'data.pkl', 'wb') as pkl_file:
    pickle.dump(A, pkl_file)

# show the file on disk and its size (mac/linux)
# ll $PATH*

with open(PATH+'data.pkl', 'rb') as pkl_file:
    B = pickle.load(pkl_file)
A[:3]
B[:3]

# convert A and B to ndarray
# np.allclose() verifies that both contain the same data (numbers)
np.allclose(np.array(A), np.array(B))

with open(PATH+'data.pkl', 'wb') as pkl_file:
    pickle.dump(np.array(A), pkl_file)
    pickle.dump(np.array(A) ** 2, pkl_file)

with open(PATH+'data.pkl', 'rb') as pkl_file:
    # retrieve the object that was stored first
    X = pickle.load(pkl_file)
    # retrieve the object that was stored second
    Y = pickle.load(pkl_file)
X[:4]
Y[:4]

with open(PATH+'data.pkl', 'wb') as pkl_file:
    pickle.dump({'X': X, 'Y': Y}, pkl_file)
with open(PATH+'data.pkl', 'rb') as pkl_file:
    data = pickle.load(pkl_file)
for key in data.keys():
    print(key, data[key][:4])

# !rm -f $PATH*


# reading and writing text files
rows = 5000
A = np.random.standard_normal((rows, 5)).round(4)
A
T = pd.date_range(start='2019/1/1', periods=rows, freq='H')
T
HEADER = 'date,no1,no2,no3,no4,no5\n'
with open(PATH+'data.csv', 'w', encoding='utf-8') as csv_file:
    csv_file.write(HEADER)
    for t_, (no1, no2, no3, no4, no5) in zip(T, A):
        S = f'{t_},{no1},{no2},{no3},{no4},{no5}\n'
        csv_file.write(S)

with open(PATH+'data.csv', 'r', encoding='utf-8') as csv_file:
    for i in range(5):
        print(csv_file.readline(), end='')

with open(PATH+'data.csv', 'r', encoding='utf-8') as csv_file:
    content = csv_file.readlines()
    print(content[:5])

with open(PATH+'data.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)       # iterator of lists
    lines = [line for line in csv_reader]
lines[:5]

with open(PATH+'data.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)   # iterator of dicts
    lines = [line for line in csv_reader]
lines[:5]


# working with sql databases
con = sq3.connect(PATH+'numbs.db')
query = 'CREATE TABLE numbs (Date date, No1 real, No2 real)'
con.execute(query)
# commit changes
con.commit()
# define a short alias for con.execute() method
Q = con.execute
# fetch metainformation about the database
# showing the just-created table as the single object
Q('SELECT * FROM sqlite_master').fetchall()

now = datetime.datetime.now()
Q('INSERT INTO numbs VALUES(?, ?, ?)', (now, 0.12, 7.3))

np.random.seed(100)
data = np.random.standard_normal((10000, 2)).round(4)

for row in data:
    now = datetime.datetime.now()
    Q('INSERT INTO numbs VALUES(?, ?, ?)', (now, row[0], row[1]))
con.commit()

Q('SELECT * FROM numbs').fetchmany(4)
Q('SELECT * FROM numbs WHERE no1 > 0.5').fetchmany(4)

pointer = Q('SELECT * FROM numbs')
for i in range(3):
    print(pointer.fetchone())

rows = pointer.fetchall()
rows[:3]

Q('DROP TABLE IF EXISTS numbs')
Q('SELECT * FROM sqlite_master').fetchall()
con.close()


# writing and reading numpy arrays
# create an ndarray object with datetime as dtype
dtimes = np.arange('2019-01-01 10:00:00', '2025-12-31 22:00:00',
                   dtype='datetime64[m]')
len(dtimes)
# define the special dtype object for the structured array
dty = np.dtype([('Date', 'datetime64[m]'), ('No1', 'f'), ('No2', 'f')])
# instantiate an ndarray object with the special dtype
data = np.zeros(len(dtimes), dtype=dty)
# populate the date column
data['Date'] = dtimes
# the dummy data sets
A = np.random.standard_normal((len(dtimes), 2)).round(4)
data['No1'] = A[:, 0]
data['No2'] = A[:, 1]
data.nbytes
# the size on disk is hardly larger than in memory due to binary storage
np.save(PATH+'array', data)
np.load(PATH+'array.npy')

data = np.random.standard_normal((10000, 6000)).round(4)
data.nbytes
np.save(PATH+'array', data)
np.load(PATH+'array.npy')
