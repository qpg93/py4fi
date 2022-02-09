""" pandas dataframe basics """
import numpy as np
import pandas as pd
from pylab import plt, mpl

# first step with the dataframe class
df = pd.DataFrame([10, 20, 30, 40],
                  columns=['numbers'],
                  index=['a', 'b', 'c', 'd'])
print('df:', df)
print('df.index:', df.index)
print('df.columns:', df.columns)
print("df.loc['c']:", df.loc['c'])
print("df.loc[['a', 'd']]:", df.loc[['a', 'd']])
print("df.iloc[1:3]:", df.iloc[1:3])  # index position
print('df.sum():', df.sum())
print('df.apply(lambda x: x**2):', df.apply(lambda x: x**2))
print('df ** 2:', df ** 2)

df['floats'] = (1.5, 2.5, 3.5, 4.5)
print('df:', df)

df['names'] = pd.DataFrame(['Yves', 'Sandra', 'Lilli', 'Henry'],
                           index=['d', 'a', 'b', 'c'])
print('df:', df)

print('df.append:',
      df.append({'numbers': 100, 'floats': 5.75, 'names': 'Jil'},
                ignore_index=True))
print('df:', df)

df = df.append(pd.DataFrame({'numbers': 100, 'floats': 5.75, 'names': 'Jil'},
                            index=['y', ]))
print('df:', df)

df = df.append(pd.DataFrame({'names': 'Liz'}, index=['z', ]),
               sort=False)
print('df:', df)
print('df.dtypes:', df.dtypes)

print('df mean:', df[['numbers', 'floats']].mean())
print('df std:', df[['numbers', 'floats']].std())

# second steps with the dataframe class
np.random.seed(100)
a = np.random.standard_normal((9, 4))
print('a:', a)

df = pd.DataFrame(a)
print('df:', df)
df.columns = ['No1', 'No2', 'No3', 'No4']
print('df:', df)
print('df["No2"].mean():', df['No2'].mean())

# 9 data entries in 4 columns correspond to month-end data,
# beginning in january 2019
dates = pd.date_range('2019-1-1', periods=9, freq='M')
print('dates:', dates)

df.index = dates
print('df:', df)
print('df.values:', df.values)
print('np.array(df):', np.array(df))

# basic analytics
print('df.info():', df.info())
print('df.describe():', df.describe())
print('df.sum():', df.sum())
print('df.mean():', df.mean())
print('df.mean(axis=0):', df.mean(axis=0))
print('df.mean(axis=1):', df.mean(axis=1))
# column-wise cumulative sum (starting at first index position)
print('df.cumsum():', df.cumsum())
# dataframe objects also understand numpy universal functions
print('np.mean(df):', np.mean(df))
print('np.log(df):', np.log(df))
print('np.sqrt(abs(df)):', np.sqrt(abs(df)))
print('np.sqrt(abs(df)).sum():', np.sqrt(abs(df)).sum())
print('100 * df + 100:', 100 * df + 100)

# basic visualization
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'
df.cumsum().plot(lw=2.0, figsize=(10, 6))
df.plot.bar(figsize=(10, 6), rot=15)  # rot: rotation of x-ticks

# the series class: only a single column of data
print('type(df):', type(df))
S = pd.Series(np.linspace(0, 15, 7), name='series')
print('S:', S)
print('type(S):', type(S))
s = df['No1']
print('s:', s)
print('type(s):', type(s))
print('s.mean():', s.mean())

s.plot(lw=2.0, figsize=(10, 6))

# groupby operations
