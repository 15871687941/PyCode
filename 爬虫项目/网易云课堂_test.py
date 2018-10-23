import requests
from bs4 import BeautifulSoup
from pprint import pprint
start_url = "https://study.163.com"
response = requests.get(start_url)
html_code = response.text
# print(html_code)
soup = BeautifulSoup(html_code, "lxml")
as_ = soup.select("div#j-nav-catedialog > div.cateleft div.items > div.item a.first")
print(as_)
# activityId	0
# frontCategoryId	400000000154043
# keyword
# orderType	50
# pageIndex	1
# pageSize	50
# priceType	-1
# relativeOffset	0
# searchTimeType	-1
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# activityId	0
# frontCategoryId	400000001263002
# keyword
# orderType	50
# pageIndex	1
# pageSize	50
# priceType	-1
# relativeOffset	0
# searchTimeType	-1
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# activityId	0
# frontCategoryId	400000001316004
# keyword
# orderType	50
# pageIndex	1
# pageSize	50
# priceType	-1
# relativeOffset	0
# searchTimeType	-1
"Host": "study.163.com",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0",
"Accept": "application/json",
"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Accept-Encoding": "gzip, deflate, br",
"Referer": "https://study.163.com/category/office-productivity",
"edu-script-token": "b486df040d224013aed0aa554ca361df",
"Content-Type": "application/json",
"Content-Length": "162",
"Connection": "keep-alive",
"Cache-Control": "max-age=0, no-cache",
"Pragma": "no-cache",
