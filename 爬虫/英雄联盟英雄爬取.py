# coding: utf-8
import requests, re, os, json
from urllib.request import urlretrieve
from lxml import etree

start_url = "http://lol.qq.com/biz/hero/champion.js"
# image_url = "http://ossweb-img.qq.com/images/lol/img/champion/{}.png"
skin_url = "http://ossweb-img.qq.com/images/lol/web201310/skin/big{}.jpg"
skin_urls = {}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
}
response = requests.get(start_url, headers=headers)
result = response.content.decode("unicode-escape")
champion = re.search('"data":(.*?),"version"', result)
info = "".join(champion.groups())
heros = json.loads(info)
print(type(heros))
for hero in heros.values():
    download_urls = []
    for i in range(20):
        num = str(i)
        if len(num) == 1:
            num = "00" + num
        else:
            num = "0" + num
        download_urls.append(skin_url.format((hero['key'] + num)))
    skin_urls[hero['name'] + "(" + hero['title'] + ")"] = download_urls
print(skin_urls)
base_path = r"H:\爬虫下载文件\英雄联盟英雄皮肤"
if not os.path.exists(base_path):
    os.mkdir(base_path)
count = 0
for name, urls in skin_urls.items():
    print("正在下载{}的皮肤...".format(name))
    for url in urls:
        response = requests.get(url, headers=headers)
        count += 1
        if response.status_code == 200:
            with open(os.path.join(base_path, name + str(count) + ".jpg"), "wb") as fp:
                fp.write(response.content)
            print("{}的第{}个皮肤下载成功！".format(name, str(count)))
        else:
            count = 0
            break





