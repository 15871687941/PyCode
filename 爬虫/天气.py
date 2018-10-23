import requests
# 在爬取前，应该检测网页是否有回应
start_url = "http://d1.weather.com.cn/ca\
lendar_new/2018/101200201_201806.html?_=1530958631818"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Ge\
    cko) Chrome/65.0.3325.146 Safari/537.36",
    "Host": "d1.weather.com.cn"
}

response = requests.get(url=start_url, headers=headers)
print(response.text)