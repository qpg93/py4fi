""" high-frequency data """
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

tick = pd.read_csv('../data/fxcm_eur_usd_tick_data.csv',
                   index_col=0, parse_dates=True)
tick.info()
# calculate the mid price for every data row
tick['Mid'] = tick.mean(axis=1)
tick['Mid'].plot(figsize=(10, 6))

# resample the tick data to 5-minute bar data
# can be used to backtest algorithmic trading strategies
# or to implement a technical analysis
tick_resam = tick.resample(rule='5min', label='right').last()
tick_resam.head()
tick_resam['Mid'].plot(figsize=(10, 6))
