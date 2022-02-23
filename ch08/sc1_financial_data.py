""" financial data with time series """
import numpy as np
import pandas as pd
from pylab import mpl, plt
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

# data import
FILENAME = '../data/tr_eikon_eod_data.csv'
data = pd.read_csv(FILENAME,
                   index_col=0,         # first column as index
                   parse_dates=True)    # index values are of type datetime
data.head()
data.tail()
data.plot(figsize=(10, 12), subplots=True)

instruments = ['Apple Stock',
               'Microsoft Stock',
               'Intel Stock',
               'Amazon Stock',
               'Goldman Sachs Stock',
               'SPDR S&P 500 ETF Trust',
               'S&P 500 Index',
               'VIX Volatility Index',
               'EUR/USD Exchange Rate',
               'Gold Price',
               'VanEck Vectors Gold Miners ETF',
               'SPDR Gold Trust']
for ric, name in zip(data.columns, instruments):
    print(f'{ric:8s} | {name}')

# summary statistics
data.info()
data.describe().round(2)
data.mean()
data.aggregate([min, np.mean, np.std, np.median, max]).round(2)

# change over time
data.diff().round(2)    # absolute changes between two index values
data.diff().mean()
data.pct_change().round(3).head()   # percentage change
data.pct_change().mean().plot(kind='bar', figsize=(10, 6))

rets = np.log(data / data.shift(1))  # log returns in vectorized fashion
rets.head().round(3)
# cumulative log returns over time
# first cumsum() is called, then np.exp() is applied to the results
rets.cumsum().apply(np.exp).plot(figsize=(10, 6))

# resampling
# eod data gets resampled to weekly time intervals
data.resample('1w', label='right').last().head()
# monthly
data.resample('1m', label='right').last().head()
# cumulative log returns over time
rets.cumsum().apply(np.exp).resample('1m', label='right').last(
        ).plot(figsize=(10, 6))

# ============================================================================
# when resampling
# pandas takes by default the left label (or index value) of the interval
# to be financially consistent, make sure to use the right label (index value)
# and in general the last available data point in the interval
# otherwise, a foresight bias might sneak into the financial analysis
