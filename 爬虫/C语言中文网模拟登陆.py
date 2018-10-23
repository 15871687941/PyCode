import requests
import sys
import io
from urllib.parse import unquote

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
# 登录网址
login_url = "http://vip.biancheng.net/login.php"
# 设置请求头
headers = {
    "Host": "http://vip.biancheng.net/login.php",
    "Referer": "http://vip.biancheng.net/login.php",
    "User-Agent": "http://vip.biancheng.net/login.php"
}
# 登录时需要POST的数据
data = {
    "password": "wangtianyu",
    "submit": "登录",
    "username": "ZYK"
}
# 构造Session
session = requests.Session()
# 在session中发送登录请求，此后这个session里就存储了session
resp = session.post(url=login_url, data=data)
print(session.cookies.get_dict())
# print(unquote(session.cookies.get_dict()['PHPSESSID']))
url1 = "http://vip.biancheng.net/get_arc_body.php?callback=jQuery1720022189255789\
358153_1530929545062&aid=3163&v=3.993&_=1530929545120"
response = session.get("http://vip.biancheng.net/get_arc_body.php?aid=3163&v=3.993")
print(unquote(response.text))

# data = re.search('"data":"(.*?)"}\)$', response.text)
# print(data.groups(1))
# with open("C:\\Users\\God\\Desktop\\C语言中文网.html","wb") as fp:
#    fp.write(response.content)
