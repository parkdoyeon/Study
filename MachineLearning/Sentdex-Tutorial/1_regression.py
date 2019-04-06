import pandas as pandas
import quandl
import math

df = quandl.get('WIKI/GOOGL')
#print(df.head())

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close','Adj. Volume']]
#High-Low는 가격 변동을 보여줌
df['HL_PCT'] =  (df['Adj. High'] - df['Adj. Close'])/df['Adj. Close'] * 100.0
df['PCT_Change'] =  (df['Adj. Close'] - df['Adj. Open'])/df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_Change', 'Adj. Volume']] 
#volume: 하루에 이뤄진 거래 횟수
#print(df.head())

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)
#ML에서는 반드시 데이터가 있어야한다. 다른 데이터를 다 날릴순 없으니까

# 예측하려는 데이터의 갯수.
# 전체의 10% 데이터를 예측하려함, 여기서 소수점이 나오면 안되니까 ceil 함수로 정수 올림해버린다.
forecast_out = int(math.ceil(0.1*len(df)))

# 10일 뒤의 마감가격이 되는것.
df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
#print(df.head())
print(df.tail())
