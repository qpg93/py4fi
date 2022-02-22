""" interactive 2d plotting """
import numpy as np
import pandas as pd
import cufflinks as cf
import plotly.offline as plyo
# from plotly.offline import download_plotlyjs, init_notebook_mode

# turn on the notebook plotting mode
plyo.init_notebook_mode(connected=True)
# init_notebook_mode(connected=True)
cf.go_offline()
cf.set_config_file(offline=True, world_readable=True)

# %matplotlib inline
np.random.seed(1)

# basic plots
a = np.random.standard_normal((250, 5)).cumsum(axis=0)
# frequency: business daily
index = pd.date_range('2019-1-1', freq='B', periods=len(a))
df = pd.DataFrame(100 + 5 * a,
                  columns=list('abcde'),
                  index=index)
df.head()

plyo.iplot(df.iplot(asFigure=True), image='png', filename='ply_01')


plyo.iplot(df[['a', 'b']].iplot(asFigure=True,
                                theme='polar',
                                title='a time series plot',
                                xTitle='date',
                                yTitle='value',
                                mode={'a': 'markers', 'b': 'lines+markers'},
                                symbol={'a': 'circle', 'b': 'diamond'},
                                size=3.5,
                                colors={'a': 'blue', 'b': 'magenta'}),
           image='png', filename='ply_02')

plyo.iplot(df.iplot(kind='hist',
                    subplots=True,
                    bins=15,
                    asFigure=True),
           image='png', filename='ply_03')

# financial plots
raw = pd.read_csv('../data/fxcm_eur_usd_eod_data.csv',
                  index_col=0, parse_dates=True)
raw.info()

quotes = raw[['AskOpen', 'AskHigh', 'AskLow', 'AskClose']]
quotes = quotes.iloc[-60:]
quotes.tail()

qf = cf.QuantFig(quotes, title='eur/usd exchange rate',
                 legend='top', name='eur/usd')
plyo.iplot(qf.iplot(asFigure=True), image='png', filename='qf_01')

qf.add_bollinger_bands(periods=15, boll_std=2)
plyo.iplot(qf.iplot(asFigure=True), image='png', filename='qf_02')

qf.add_rsi(periods=14, showbands=False)
plyo.iplot(qf.iplot(asFigure=True), image='png', filename='qf_03')
