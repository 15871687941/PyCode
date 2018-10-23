# encoding = utf-8
from selenium import webdriver
import time
import requests
import random
import re
from urllib.parse import urlencode
import json
from pprint import pprint

post = {}

driver = webdriver.Chrome(r"I:\Anaconda\Scripts\chromedriver")
driver.get('https://mp.weixin.qq.com/')
time.sleep(1)
# 用户名
driver.find_element_by_name("account").clear()
driver.find_element_by_name("account").send_keys("1806521378@qq.com")
# 密码
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("asd2743075")
# 确定
driver.find_element_by_class_name("btn_login").click()
# 扫描二维码
time.sleep(15)
# driver.get('https://mp.weixin.qq.com/')
cookies_items = driver.get_cookies()
for cookie_item in cookies_items:
    post[cookie_item["name"]] = cookie_item["value"]
url = "https://mp.weixin.qq.com/cgi-bin/appmsg?"
      # "token=1553773092&lang=zh_CN&f=json&ajax=1&random=0.20920657848965996&action=list_ex&begin=5&count=5&query=&fakeid=MzI5MjQxOTk3Mg%3D%3D&type=9"
token = re.findall("token=(\d+)$", driver.current_url)[0]
query = {
    "token": token,
    "lang":  "zh_CN",
    "f": "json",
    "ajax": "1",
    "random": random.random(),
    "action": "list_ex",
    "begin": "0",
    "count": "5",
    "query": "",
    "type": "9"
}
response = requests.get(url=(url + urlencode(query)), cookies=post)
print(response.text)
time.sleep(5)
driver.quit()


