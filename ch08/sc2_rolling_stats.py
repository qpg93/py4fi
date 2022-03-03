""" rolling statistics (financial indicators, financial studies) """
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'


FILENAME = '../data/tr_eikon_eod_data.csv'
data = pd.read_csv(FILENAME,
                   index_col=0,         # first column as index
                   parse_dates=True)    # index values are of type datetime
SYM = 'AAPL.O'
data = pd.DataFrame(data[SYM]).dropna()
data.tail()

# number of index values to include
WINDOW = 20
# calculate the rolling minimum value
data['min'] = data[SYM].rolling(window=WINDOW).min()
data['mean'] = data[SYM].rolling(window=WINDOW).mean()
data['std'] = data[SYM].rolling(window=WINDOW).std()
data['median'] = data[SYM].rolling(window=WINDOW).median()
data['max'] = data[SYM].rolling(window=WINDOW).max()
# calculate the exponentially weighted moving average,
# with decay in terms of a half life of 0.5
data['ewma'] = data[SYM].ewm(halflife=0.5, min_periods=WINDOW).mean()

data.dropna().head()
ax = data[['min', 'mean', 'max']].iloc[-200:].plot(
        figsize=(10, 6),
        style=['g--', 'r--', 'g--'],
        lw=0.8)
data[SYM].iloc[-200:].plot(ax=ax, lw=2.0)

# calculate the values for the shorter-term SMA
data['SMA1'] = data[SYM].rolling(window=42).mean()
# calculate the values for the longer-term SMA
data['SMA2'] = data[SYM].rolling(window=252).mean()
data[[SYM, 'SMA1', 'SMA2']].tail()
data[[SYM, 'SMA1', 'SMA2']].plot(figsize=(10, 6))

data.dropna(inplace=True)
data['positions'] = np.where(data['SMA1'] > data['SMA2'],
                             1,     # if condition, go long on the stock
                             -1)    # otherwise, go short on the stock
ax = data[[SYM, 'SMA1', 'SMA2', 'positions']].plot(figsize=(10, 6),
                                                   secondary_y='positions')
ax.get_legend().set_bbox_to_anchor((0.25, 0.85))
