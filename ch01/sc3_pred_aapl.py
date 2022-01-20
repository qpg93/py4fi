import numpy as np
import pandas as pd
from sklearn.svm import SVC

data = pd.read_csv('../data/tr_eikon_eod_data.csv',
                   index_col=0,
                   parse_dates=True)
data = pd.DataFrame(data['AAPL.O'])
data['Returns'] = np.log(data / data.shift())
data.dropna(inplace=True)
data.head()

LAGS = 6
cols = []
for lag in range(1, LAGS + 1):
    col = f'lag_{lag}'
    data[col] = np.sign(data['Returns'].shift(lag))
    cols.append(col)
data.dropna(inplace=True)

model = SVC(gamma='auto')

model.fit(data[cols], np.sign(data['Returns']))

data['Prediction'] = model.predict(data[cols])

data['Strategy'] = data['Prediction'] * data['Returns']

data[['Returns', 'Strategy']].cumsum().apply(np.exp).plot(figsize=(10, 6))
