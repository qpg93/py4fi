""" correlation analysis """
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

raw = pd.read_csv('../data/tr_eikon_eod_data.csv',
                  index_col=0,
                  parse_dates=True)
data = raw[['.SPX', '.VIX']].dropna()
data.tail()
data.plot(subplots=True, figsize=(10, 6))

# when plotting the 2 time series in a single plot and with adjusted scalings
# the stylized fact of negative correlation between the 2 indices
# becomes evident through simple visual inspection
data.loc[:'2012-12-31'].plot(secondary_y='.VIX', figsize=(10, 6))

# logarithmic returns
rets = np.log(data / data.shift(1))
rets.head()
rets.dropna(inplace=True)
rets.plot(subplots=True, figsize=(10, 6))
pd.plotting.scatter_matrix(rets,
                           alpha=0.2,
                           diagonal='hist',
                           hist_kwds={'bins': 35},
                           figsize=(10, 6))


# ols regresion (ordinary least-squares)
# linear ols regression
reg = np.polyfit(rets['.SPX'], rets['.VIX'], deg=1)
# this plots the log returns as a scatter plot
ax = rets.plot(kind='scatter', x='.SPX', y='.VIX', figsize=(10, 6))
# add the linear regression line
ax.plot(rets['.SPX'], np.polyval(reg, rets['.SPX']), 'r', lw=2)

# correlation
rets.corr()     # correlation matrix for the whole dataframe
# plot the rolling correlation over time
ax = rets['.SPX'].rolling(window=252).corr(rets['.VIX']).plot(figsize=(10, 6))
# add static value as horizontal line
ax.axhline(rets.corr().iloc[0, 1], c='r')
