#ToDo
#グラフ描画(円、チャート)→MPandroidchart
#株価データベース→スクレイピング、firebase
#所有株入力→UI考える
#ユーザーデータ保存→sql
#Twitter投稿
#米国株対応

#スクレイピングをしFirebaseにデータを格納する
#スクレイピング(日本株)

# import pandas as pd

# df = pd.read_excel('data_j.xls')

# print(df["コード"])

# s = df["コード"]

# list_s = s.values.tolist()
# print(list_s)

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import pandas as pd

# def extract(code):
#     try:
#         print(code)
#         tgt = 'https://kabutan.jp/stock/kabuka?code=' + str(code)
#         html = urlopen(tgt)
#         bsObj = BeautifulSoup(html, 'html.parser')
#         table = bsObj.findAll('table', {'class':'stock_kabuka0'})[0]
#         print(table)
#         rows = table.findAll('tr')
#         for row in rows:
#             rec = []
#             for cell in row.findAll(['td', 'th']):
#                 rec.append(cell.get_text())
#                 # print(rec)
#             del rec[5:7]
#             # rec.insert(0, str(code) + '.JP')
#             rec.insert(0, str(code))
#         dish.append(rec)
#         return 'Success'
#     except Exception as e:
#         return str(code) + ': ' + str(e)

# TickerSymbol = [4755,6758]
# # TickerSymbol = list_s
# dish = []
# [extract(i) for i in TickerSymbol]
# pd.DataFrame(dish).rename(columns={0: 'code', 1: 'Date', 2:'Open', 3: 'High', 4: 'Low', 5:'Close', 6: 'Volume'})
# print(dish[0][0])

#日本株過去データ取得
# import pandas_datareader as pdr

# pdr =pdr.stooq.StooqDailyReader(symbols='4755.jp', start='AUG-01-2010', end="SEP-21-2020").read().sort_values(by='Date',ascending=True)
# print(pdr)


#Firebaseにデータを格納
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('trading-stocks-portfolio-firebase-adminsdk-2qlwo-0d6a2017a1.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://trading-stocks-portfolio.firebaseio.com/',
    'databaseAuthVariableOverride': {
        'uid': 'my-service-worker'
    }
})

##databaseに初期データを追加する
users_ref = db.reference('/stocks')

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

for i in range(1,2):
    tgt = "https://kabuoji3.com/stock/?page=" + str(i)
    html = urlopen(tgt)
    bsObj = BeautifulSoup(html, 'html.parser')
    test = bsObj.findAll('p', {'class':'pgp'})
    print(test)
    # table = bsObj.findAll('table', {'class':'stock_table'})[0]
    # rows = table.findAll('tbody')
    # count = 0
    # child = "test"
    # for cell in rows[0].findAll('td'):
    #     tmp = cell.get_text()
    #     if(count % 6 == 0):
    #         print("##########")
    #         print(tmp[:4])
    #         print(tmp[5:])
    #         child = tmp[:4]
    #         users_ref.child(child).set({
    #             "name":tmp[5:]
    #         })
    #     elif((count+1) % 6 == 0):
    #         print(tmp)
    #         users_ref.child(child).update({
    #             "close":tmp
    #         })
    #     count = count + 1




# users_ref.child(dish[1][0]).set({
#     "date":dish[1][1],
#     "close":dish[1][5]
# })

# users_ref.set({
#     dish[0][0]:{
#         "date":dish[0][1],
#         "close":dish[0][5]
#     }
# })

# users_ref.set({
#     'user001': {
#         'date_of_birth': 'June 23, 1984',
#         'full_name': 'Sazae Isono'
#         },
#     'user002': {
#         'date_of_birth': 'December 9, 1995',
#         'full_name': 'Tama Isono'
#         }
#     })

# # databaseにデータを追加する
# users_ref.child('user003').set({
#     'date_of_birth': 'Aug 23, 1980',
#     'full_name': 'Masuo Isono'
#     })

# #データを取得する
# print(users_ref.get())
