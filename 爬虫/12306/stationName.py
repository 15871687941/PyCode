import requests, re, json, pickle
# 1.找到对应的url，发送请求，并获取信息
station_name_url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9061"
response = requests.get(station_name_url)
print(response.text)

# 2.正则表达式提取信息
result = re.findall("[a-z]{3}\|(.*?)\|([A-Z]{3})\|[a-z]+\|[a-z]+\|[0-9]{1,4}", response.text)
stationName = {}
for cw, sw in result:
    stationName[cw] = sw
with open("stationName.pickle", "wb") as fp:
    pickle.dump(stationName, fp)

