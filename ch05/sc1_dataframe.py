""" pandas dataframe basics """
import pandas as pd

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
