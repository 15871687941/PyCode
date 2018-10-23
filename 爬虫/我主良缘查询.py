# coding: utf-8
# http://www.lovewzly.com/api/user/pc/list/search?startage=21&endage=30&gender=2&cityid=180&startheight=161&endheight=170&marry=1&astro=1&lunar=1&education=10&salary=2&page=1
# base_url = "http://www.lovewzly.com/api/user/pc/list/search"
# params: startage, endage, gender, cityid, startheight, endheight,
# marry, astro(星座), lunar(属相), education(受教育程度), salary(工资),
# page
# 1、获取搜索信息
# 2、构建url并解析网页信息
# 3、显示或存储
import json
import sqlite3 as sq3
import requests
from urllib.parse import urlencode
def get_input_info():
    data = {}
    age = int(input("请输入具体年龄信息(21~40)："))
    gender = input("请输入性别信息（男或女）：")
    cityid = 180  # (武汉)
    height = int(input("请输入身高信息："))
    marry = 1  # 未婚1 离异3 丧偶4
    # pages = 20  # 假设最多有20页
    if age in list(range(21, 31)):
        startage = 21
        endage = 30
    elif age in list(range(31, 41)):
        startage = 31
        endage = 40
    else:
        startage = 21
        endage = 30
    if height in list(range(0, 151)):
        startheight = 0
        endheight = 150
    elif height in list(range(151, 161)):
        startheight = 151
        endheight = 160
    elif height in list(range(161, 171)):
        startheight = 161
        endheight = 170
    elif height in list(range(171, 181)):
        startheight = 171
        endheight = 180
    elif height in list(range(181, 191)):
        startheight = 181
        endheight = 190
    else:
        startheight = 190
        endheight = 250
    if gender == "男":
        gender = 1
    else:
        gender = 2
    data["startage"] = startage
    data["endage"] = endage
    data["gender"] = gender
    data["cityid"] = cityid
    data["startheight"] = startheight
    data["endheight"] = endheight
    data["marry"] = marry
    return data


def get_urls(pages=20, **data):
    base_url = "http://www.lovewzly.com/api/user/pc/list/search?"
    start_urls = []
    for page in range(1, pages + 1):
        start_urls.append(base_url + urlencode(data))
    return start_urls


def get_page_information(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        informations = json.loads(response.content.decode())
        print(type(informations))
        return informations
    else:
        return None


if __name__ == '__main__':
    connection = sq3.connect("blindDate.db")
    cursion = connection.cursor()
    data = get_input_info()
    urls = get_urls(**data)
    for url in urls:
        infos = get_page_information(url)
        if infos is not None:
            for girl in infos["data"]["list"]:
                print(girl["userid"], girl["username"], girl["gender"], girl["birthdayyear"], girl["height"], girl["province"], girl["city"], girl["education"], girl["monolog"], girl["avatar"])
                cursion.execute('''
                insert into girl(
                userid, 
                username,
                gender,
                birthday,
                height,
                province,
                city,
                education,
                monolog,
                image
                ) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (girl["userid"], girl["username"], girl["gender"], girl["birthdayyear"], girl["height"], girl["province"], girl["city"], girl["education"], girl["monolog"], girl["avatar"]))

        else:
            break
    cursion.close()
    connection.commit()
    connection.close()








