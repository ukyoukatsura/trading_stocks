#ライブラリインポート



#1年分の1分足のデータ量を調べる
#Firebaseを試す
#MT5 API から直近のデータを取得し、チャート化。（リアルタイムにアプリから取得）
#Firebaseでwebアプリ用ドメイン取得方法


# import oandapyV20
# from oandapyV20.endpoints.instruments import InstrumentsCandles
# import mplfinance as mpf
# import datetime
# import pandas as pd
# import numpy as np

# #アカウント情報
# accountID = "101-009-16519519-001" 
# access_token = "2188a73dcf10e8e04751744b53128477-11fb353f1a445260b990f0e41856882c" 
 
# #APIに接続
# api = oandapyV20.API(access_token = access_token, environment = "practice")
 
# #取得したいデータ情報
# r = InstrumentsCandles(instrument="USD_JPY",params={"granularity":"M1"})
 
# #APIへデータ要求
# api.request(r)
 
# #「data」変数に取得データを格納
# data = r.response

# #「data」をmplfinanceに読み込ませるために整える
# ohlc = []
# for r in data["candles"]:
#     time = r["time"].replace(".000000000Z", "") # 必要のない部分の削除
#     time = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S")    # datetimeに変換
#     r["mid"]["time"] = time
#     ohlc.append(r["mid"])
# df = pd.DataFrame(ohlc)
# df = df[["time", "o", "h", "l", "c"]]
# df = df.set_index("time")
# df.columns = ['Open', 'High', 'Low', 'Close']
# df = df.astype(np.float64)
# print(df)
# mpf.plot(df,type='candle', mav=(5, 25, 75))





from datetime import datetime
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
 
# import the 'pandas' module for displaying data obtained in the tabular form
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display
# import pytz module for working with time zone
import pytz
 
# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()
 
# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
# create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2020, 8, 1, tzinfo=timezone)
utc_to = datetime(2020, 8, 30, hour = 13, tzinfo=timezone)
# get bars from USDJPY M5 within the interval of 2020.01.10 00:00 - 2020.01.11 13:00 in UTC time zone
rates = mt5.copy_rates_range("USDJPY", mt5.TIMEFRAME_M1, utc_from, utc_to)
 
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
 
# display each element of obtained data in a new line
print("Display obtained data 'as is'")
counter=0
for rate in rates:
    counter+=1
    if counter<=10:
        print(rate)
 
# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(rates)
# convert time in seconds into the 'datetime' format
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
 
# display data
print("\nDisplay dataframe with data")
print(rates_frame)
rates_frame.to_csv("fx_1month_M1.csv")