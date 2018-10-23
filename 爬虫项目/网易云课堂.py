import requests
import pymongo
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from pprint import pprint
import time


def get_page(url):
    response = requests.get(url)
    return response.text


def post_page(post_url, id_):
    header = {
        "Host": "study.163.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0"
    }
    params = {
        "activityId": "0",
        "frontCategoryId": str(id_),
        "keyword": "",
        "orderType": "50",
        "pageIndex": "1",
        "pageSize": "50",
        "priceType": "-1",
        "relativeOffset": "0",
        "searchTimeType": "-1"
    }
    session = requests.Session()
    session.get(start_url)
    response = session.post(post_url, data=params, headers=header)
    print(response.text)
    # result = response.json()
    # print(result)
    return 1


def get_crawl_urls(strat_url):
    ids = []
    crawl_urls = []
    html_code = get_page(start_url)
    soup = BeautifulSoup(html_code, "lxml")
    divs_ = soup.select("div.j-pic.f-dn")
    for div_ in divs_:
        if len(ids) < 9:
            ids.append(div_.attrs["data-id"])
    ids.reverse()
    as_ = soup.select("div#j-nav-catedialog > div.cateleft div.items > div.item a.first")
    # print(as_)
    for a_ in as_:
        url = dict()
        url["name"] = a_.text.strip()
        url["href"] = start_url + a_.attrs["href"]
        url["id"] = ids.pop()
        crawl_urls.append(url)
    # print(crawl_urls)
    return crawl_urls


def parse(html_code):
    pass


if __name__ == '__main__':
    start_url = "https://study.163.com"
    post_url = "https://study.163.com/p/search/studycourse.json"
    get_crawl_urls(start_url)
    # datas = []
    # 1、得到要提取信息的网页
    crawl_urls = get_crawl_urls(start_url)
    # 2、提取信息
    for crawl_url in crawl_urls:
        data = post_page(post_url, crawl_url["id"])
        # datas.extend(data)
    # pprint(datas)
    # # # 3、数据可视化
    # # show_datas(datas)
    # # # 4、存储数据
    # # store_database(datas)

