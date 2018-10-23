import requests
from bs4 import BeautifulSoup
import  re
start_url = 'http://www.zhaoxiaoshuo.com/all.php?c=0&o=0&s=0&f=2&l=0&page=1'
headers = {
    "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Mobile Safari/537.36'
}
response = requests.get(start_url, headers=headers)
print(type(response))
# print(response.text)
soup = BeautifulSoup(response.text, "lxml")
# max_page = soup.select(".pages a")[4].text
# 最大页
# max_page = re.search("\d+", soup.select(".pages a")[4].text)
# url
# start_url = start_url.replace("page=1", "page=2")
# print(start_url)
index = soup.select(".clearfix")[2]
print(index)
