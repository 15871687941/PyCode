# coding = utf-8
# 车次 出发站 到达站 出发时间 到达时间 历时 一等座 二等座 软卧 动卧 硬卧 软座 硬座 无座
#  3     6     7      8      9     10   31   30    23      28      29  26
import requests, json, sys, pickle
from colorama import Fore, Back, Style
# import pandas as pd
# python station_data.py 襄阳东 武昌 2018-08-01
from prettytable import PrettyTable
# print(type(sys.argv[0]), sys.argv[1], sys.argv[2])
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
}
url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-08-01&leftTicketDTO.from_station=XFN&leftTicketDTO.to_station=WHN&purpose_codes=ADULT"
stationName = {}
with open("stationName.pickle", "rb") as fp:
    stationName = pickle.load(fp)
    print(stationName)
    url.format(sys.argv[3], stationName[sys.argv[1]], stationName[sys.argv[2]])
    # print(url)
response = requests.get(url, headers=headers)
# print(response.text)
table = PrettyTable(["序号", "车次", "出发站", "到达站", "出发时间", "到达时间", "历时", "一等座", "二等座", "硬座", "无座"])
stationName = dict(zip(stationName.values(), stationName.keys()))
for j, i in enumerate(json.loads(response.text)["data"]["result"]):
    info = []
    i = i.split("|")
    info.append(j + 1)
    info.append(i[3])
    info.append(stationName[i[6]])
    info.append(stationName[i[7]])
    info.append(i[8])
    info.append(i[9])
    info.append(i[10])
    info.append(i[31])
    info.append(i[30])
    info.append(i[29])
    info.append(i[26])
    table.add_row(info)
print(table)



