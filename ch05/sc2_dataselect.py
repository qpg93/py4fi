"""
complex selection
concatenation, joining and merging
"""
import numpy as np
import pandas as pd

np.random.seed(1)

# complex selection
data = np.random.standard_normal((10, 2))
df = pd.DataFrame(data, columns=['x', 'y'])

print('df info:', df.info())
print('df head:', df.head())
print('df tail:', df.tail())

print('df["x"] > 0.5:', df['x'] > 0.5)
print('(df["x"] > 0) & (df["y"] < 0):', (df['x'] > 0) & (df['y'] < 0))
print('(df["x"] > 0) | (df["y"] < 0):', (df['x'] > 0) | (df['y'] < 0))

print('df[df["x"] > 0]:', df[df['x'] > 0])
print('df query (x > 0):', df.query('x > 0'))
print('df[(df["x"] > 0) & (df["y"] < 0)]:', df[(df['x'] > 0) & (df['y'] < 0)])
print('df query (x > 0 & y < 0):', df.query('x > 0 & y < 0'))
print('df[(df.x > 0) | (df.y < 0)]:', df[(df.x > 0) | (df.y < 0)])

# which values are positive
print('df > 0:', df > 0)
# select all such values and put a NaN in all other places
print('df[df > 0]', df[df > 0])

# concatenation, joining and merging
df1 = pd.DataFrame(['100', '200', '300', '400'],
                   index=['a', 'b', 'c', 'd'],
                   columns=['A', ])
print('df1:', df1)

df2 = pd.DataFrame(['200', '150', '50'],
                   index=['f', 'b', 'd'],
                   columns=['B', ])
print('df2:', df2)

# concatenation
print('df1 append df2:', df1.append(df2, sort=False))
print('df1 append df2 ignore index:',
      df1.append(df2, ignore_index=True, sort=False))
print('pd concat df1 df2:', pd.concat((df1, df2), sort=False))
print('pd concat df1 df2 ignore index:',
      pd.concat((df1, df2), ignore_index=True, sort=False))

# joining
print('df1 join df2:', df1.join(df2))
print('df2 join df1:', df2.join(df1))
print('df1 join df2 how left:', df1.join(df2, how='left'))
print('df1 join df2 how right:', df1.join(df2, how='right'))
print('df1 join df2 how inner:', df1.join(df2, how='inner'))
print('df1 join df2 how outer:', df1.join(df2, how='outer'))

df = pd.DataFrame()
df['A'] = df1['A']
print('df:', df)
df['B'] = df2
print('df:', df)

df = pd.DataFrame({'A': df1['A'], 'B': df2['B']})
print('df:', df)

# merging
c = pd.Series([250, 150, 50], index=['b', 'd', 'c'])
df1['C'] = c
df2['C'] = c
print('df1:\n', df1)
print('df2:\n', df2)
print('merge df1 df2:\n', pd.merge(df1, df2))
print('merge df1 df2 on C:\n', pd.merge(df1, df2, on='C'))
print('merge df1 df2 how outer:\n', pd.merge(df1, df2, how='outer'))

print('merge df1 df2 leftonA rightonB:\n',
      pd.merge(df1, df2, left_on='A', right_on='B'))
print('merge df1 df2 leftonA rightonB outer:\n',
      pd.merge(df1, df2, left_on='A', right_on='B', how='outer'))
print('merge df1 df2 leftindex rightindex:\n',
      pd.merge(df1, df2, left_index=True, right_index=True))
print('merge df1 df2 on C leftindex:\n',
      pd.merge(df1, df2, left_index=True))

df3 = df1.merge(df2.reset_index(), on='C', how='right').set_index('index')
df3.index.name = None
print('df3:\n', df3)

df3 = df1.reset_index().merge(df2, on='C', how='right').set_index('index')
df3.index.name = None
print('df3:\n', df3)

df3 = pd.merge(df1, df2, left_index=True, right_index=True)
del df3['C_y']
df3 = df3.rename(columns={'C_x': 'C'})
print('df3:\n', df3)
