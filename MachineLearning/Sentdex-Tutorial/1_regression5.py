# sklearn 에서 더이상 cross_validation 사용 안함
# train_test_split() 호출을 위해서는 model_selection 으로 대체
#
# 아래의 코드는
#    - 학습한 결과로 미래 주가를 예측!
#   - 예측 데이터를 그래프로 출력

import pandas as pd
import quandl, math, datetime
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

df = quandl.get('WIKI/GOOGL')

df               = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
df['HL_PCT']      = (df['Adj. High']   - df['Adj. Low'])   / df['Adj. Low']   * 100.0
df['PCT_change']   = (df['Adj. Close']   - df['Adj. Open'])   / df['Adj. Open']   * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
forecast_col = 'Adj. Close'
df.fillna(-9999, inplace=True)

forecast_out = int(math.ceil(0.1*len(df))) # 며칠(forecast_out) 뒤의 데이터를 가져올지 정함
df['label'] = df[forecast_col].shift(-forecast_out)   # 데이터를 shift 시킴으로써 label 데이터를 구함( 뒤의 label은 NaN이 남음 )

X = np.array(df.drop(['label'], axis=1))
X = preprocessing.scale(X) # X의 크기를 normalize
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)
Y = np.array(df['label'])

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.2)

clf = LinearRegression(n_jobs=10)
clf.fit(X_train, Y_train)
accuracy = clf.score(X_test, Y_test)
forecast_set = clf.predict(X_lately)

# print(forecast_set, accuracy, forecast_out)

df['Forecast'] = np.nan
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400   # 86400 seconds == 1440 minutes == 24 hours == 1 day
next_unix = last_unix + one_day

for i in forecast_set:
   next_date = datetime.datetime.fromtimestamp(next_unix)
   next_unix += one_day
   df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4) # 범례 표기 위치
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()