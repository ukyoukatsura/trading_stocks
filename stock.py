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

cred = credentials.Certificate('../trading-stocks-portfolio-firebase-adminsdk-2qlwo-0d6a2017a1.json')

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
import json


import datetime
today = datetime.date.today()
print(today.strftime('%Y%m%d'))

for i in range(1,2):
    tgt = "https://kabuoji3.com/stock/?page=" + str(i)
    html = urlopen(tgt)
    bsObj = BeautifulSoup(html, 'html.parser')
    test = bsObj.findAll('p', {'class':'pgp'})
    print(test)
    table = bsObj.findAll('table', {'class':'stock_table'})[0]
    rows = table.findAll('tbody')
    count = 0
    child = "test"
    origin = "{"
    for cell in rows[0].findAll('td'):

        tmp = cell.get_text()
        if(count % 6 == 0):
            print("##########")
            print(tmp[:4])
            print(tmp[5:])
            child = tmp[:4]
            if(count != 0):
                origin = origin + ","
            origin = origin + "\"" + child + "\"" + ":" + "{" + "\"name\"" + ":" + "\"" + tmp[:4] + "\"" + ","
        elif((count+1) % 6 == 0):
            origin = origin + "\"price\"" + ":" + "\"" + tmp + "\"" + "}"
            print(tmp)
        count = count + 1
    origin = origin + "}"
    print(origin)
    # tesss = json.dumps(origin)
    json_dict = json.loads(origin)
    users_ref.set(json_dict)
        # if(count % 6 == 0):
        #     print("##########")
        #     print(tmp[:4])
        #     print(tmp[5:])
        #     child = tmp[:4]
        #     users_ref.child(child).set({
        #         "name":tmp[5:]
        #     })
        # elif((count+1) % 6 == 0):
        #     print(tmp)
        #     users_ref.child(child).update({
        #         "close":tmp
        #     })
        # count = count + 1
tea = {"1301":{"name":"1301","price":"2824"},"1305":{"name":"1305","price":"1728"},"1306":{"name":"1306","price":"1708"},"1308":{"name":"1308","price":"1692"},"1309":{"name":"1309","price":"38850"},"1311":{"name":"1311","price":"742"},"1312":{"name":"1312","price":"19540"},"1313":{"name":"1313","price":"2840"},"1320":{"name":"1320","price":"24080"},"1321":{"name":"1321","price":"24120"},"1322":{"name":"1322","price":"6980"},"1323":{"name":"1323","price":"317"},"1324":{"name":"1324","price":"130"},"1325":{"name":"1325","price":"152"},"1326":{"name":"1326","price":"18950"},"1327":{"name":"1327","price":"2753"},"1329":{"name":"1329","price":"24210"},"1330":{"name":"1330","price":"24180"},"1332":{"name":"1332","price":"450"},"1333":{"name":"1333","price":"2398"},"1343":{"name":"1343","price":"1883"},"1344":{"name":"1344","price":"720"},"1345":{"name":"1345","price":"1772"},"1346":{"name":"1346","price":"24230"},"1348":{"name":"1348","price":"1711"},"1349":{"name":"1349","price":"12740"},"1352":{"name":"1352","price":"933"},"1356":{"name":"1356","price":"1748"},"1357":{"name":"1357","price":"697"},"1358":{"name":"1358","price":"19710"},"1360":{"name":"1360","price":"1695"},"1364":{"name":"1364","price":"15070"},"1365":{"name":"1365","price":"16190"},"1366":{"name":"1366","price":"1813"},"1367":{"name":"1367","price":"13280"},"1368":{"name":"1368","price":"2537"},"1369":{"name":"1369","price":"23580"},"1375":{"name":"1375","price":"2044"},"1376":{"name":"1376","price":"1588"},"1377":{"name":"1377","price":"3785"},"1379":{"name":"1379","price":"2236"},"1380":{"name":"1380","price":"1321"},"1381":{"name":"1381","price":"3355"},"1382":{"name":"1382","price":"935"},"1383":{"name":"1383","price":"2213"},"1384":{"name":"1384","price":"679"},"1385":{"name":"1385","price":"4080"},"1386":{"name":"1386","price":"7580"},"1389":{"name":"1389","price":"7850"},"1390":{"name":"1390","price":"4260"},"1391":{"name":"1391","price":"2270"},"1392":{"name":"1392","price":"2118"},"1393":{"name":"1393","price":"34850"},"1394":{"name":"1394","price":"25200"},"1397":{"name":"1397","price":"23660"},"1398":{"name":"1398","price":"1781"},"1399":{"name":"1399","price":"1374"},"1400":{"name":"1400","price":"253"},"1401":{"name":"1401","price":"715"},"1407":{"name":"1407","price":"2864"},"1414":{"name":"1414","price":"5160"},"1417":{"name":"1417","price":"1615"},"1418":{"name":"1418","price":"287"},"1419":{"name":"1419","price":"1447"},"1420":{"name":"1420","price":"680"},"1429":{"name":"1429","price":"729"},"1430":{"name":"1430","price":"719"},"1433":{"name":"1433","price":"1310"},"1434":{"name":"1434","price":"487"},"1435":{"name":"1435","price":"232"},"1436":{"name":"1436","price":"842"},"1438":{"name":"1438","price":"1432"},"1439":{"name":"1439","price":"1187"},"1443":{"name":"1443","price":"331"},"1444":{"name":"1444","price":"3530"},"1446":{"name":"1446","price":"704"},"1447":{"name":"1447","price":"790"},"1448":{"name":"1448","price":"548"},"1449":{"name":"1449","price":"400"},"1450":{"name":"1450","price":"2400"},"1451":{"name":"1451","price":"578"},"1456":{"name":"1456","price":"5590"},"1457":{"name":"1457","price":"6550"},"1458":{"name":"1458","price":"12270"},"1459":{"name":"1459","price":"2771"},"1464":{"name":"1464","price":"10480"},"1465":{"name":"1465","price":"6420"},"1466":{"name":"1466","price":"3310"},"1467":{"name":"1467","price":"9850"},"1468":{"name":"1468","price":"6320"},"1469":{"name":"1469","price":"3320"},"1470":{"name":"1470","price":"20600"},"1471":{"name":"1471","price":"4110"},"1472":{"name":"1472","price":"1332"},"1473":{"name":"1473","price":"1673"},"1474":{"name":"1474","price":"15020"},"1475":{"name":"1475","price":"1685"},"1476":{"name":"1476","price":"1807"},"1477":{"name":"1477","price":"1730"},"1478":{"name":"1478","price":"1761"},"1481":{"name":"1481","price":"1642"},"1482":{"name":"1482","price":"2504"},"1483":{"name":"1483","price":"1607"},"1484":{"name":"1484","price":"1625"},"1486":{"name":"1486","price":"21870"},"1487":{"name":"1487","price":"19560"},"1488":{"name":"1488","price":"1799"},"1489":{"name":"1489","price":"28140"},"1490":{"name":"1490","price":"8100"},"1491":{"name":"1491","price":"38"},"1492":{"name":"1492","price":"14130"},"1493":{"name":"1493","price":"14330"},"1494":{"name":"1494","price":"16640"},"1495":{"name":"1495","price":"9960"},"1496":{"name":"1496","price":"2634"},"1497":{"name":"1497","price":"2297"},"1498":{"name":"1498","price":"12210"},"1499":{"name":"1499","price":"7960"},"1514":{"name":"1514","price":"125"},"1515":{"name":"1515","price":"4775"}}
# # tee = {
#     '1301':{
#         'name':'(株)極洋',
#         'price':'2819'
#         },
#     '1305':{
#         'name':'ダイワ 上場投信-トピックス',
#         'price':'1719'},
#     '1306':{
#         'name':'(NEXT FUNDS)TOPIX連動型上場投信',
#         'price':'1699'
#     }
# }
# tesss = json.dumps(tea)
# print(tesss)
# json_dict = json.loads(tesss)
# users_ref.set(json_dict)

# users_ref.child(dish[1][0]).set({
#     "date":dish[1][1],
#     "close":dish[1][5]
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

