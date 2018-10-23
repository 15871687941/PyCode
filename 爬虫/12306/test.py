import requests, sys, pickle, json, prettytable
from colorama import Fore
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
}
url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-08-01&leftTicketDTO.from_station=XFN&leftTicketDTO.to_station=WHN&purpose_codes=ADULT"
with open("stationName.pickle", "rb") as fp:
    stationName = pickle.load(fp)
    # url = url.format(sys.argv[3], stationName[sys.argv[1]], stationName[sys.argv[2]])
    print(url)
response = requests.get(url, headers=headers)
print(response.text)
stationName = dict(zip(stationName.values(), stationName.keys()))
table = prettytable.PrettyTable()
for j, i in enumerate(json.loads(response.text)["data"]["result"]):
    info = []
    i = i.split("|")
    j = j + 1
    if j % 2 != 0:
        info.append((Fore.GREEN + i[3] + Fore.RESET))
        info.append((Fore.GREEN + stationName[i[6]] + Fore.RESET))
        info.append((Fore.GREEN + i[8] + Fore.RESET))
    else:
        info.append((Fore.RED + i[3] + Fore.RESET))
        info.append((Fore.RED + stationName[i[6]] + Fore.RESET))
        info.append((Fore.RED + i[8] + Fore.RESET))
    info.append(stationName[i[7]])
    info.append(i[9])
    info.append(i[10])
    table.add_row(info)
print(table)