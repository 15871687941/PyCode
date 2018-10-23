import requests
from bs4 import BeautifulSoup
from pprint import pprint
import os
import sqlite3


# 1.获取要爬去的链接和要创建的目录
def get_crawl_urls(start_url):
    response = requests.get(start_url)
    if response.status_code == 200:
        html = response.text
    # print(html)
    soup = BeautifulSoup(html, "lxml")
    a_s = soup.select("#post-archives div a")
    crawl_infos = []
    for a in a_s:
        index = dict()
        index["dir"] = a.text.strip()
        index["href"] = a.attrs["href"]
        crawl_infos.append(index)
        # print(a.text, a.attrs['href'])
    # pprint(crawl_info)
    return crawl_infos


# 2.创建爬取的页面的函数
def get_page(url):
    res = requests.get(url=url)
    if res.status_code == 200:
        html = res.text
    return html


# 3.获取最大偏移量
def get_max_offset(page_code):
    soup = BeautifulSoup(page_code, "lxml")
    max_offset = soup.find(class_="prev-next-page").text
    max_offset = int(max_offset[2:-1])
    return max_offset


# 4.获取图片链接
def get_image(page_code):
    soup = BeautifulSoup(page_code, "lxml")
    img = soup.select("figure p a img")[0]
    # print(len(img))
    img_src = img.attrs["src"]
    return img_src


# 5.下载图片
def download_image(full_path, file_name, image_src):
    abs_path = full_path + "\\" + file_name
    with open(abs_path, "wb") as fp:
        response = requests.get(image_src)
        if response.status_code == 200:
            fp.write(response.content)
        else:
            return


# 6.存到数据库中
def store_database(connection, cursor, index, class_, url):
    cursor.execute("INSERT INTO PICTURE (ID, CLASS, URL) VALUES('{}', '{}', '{}')".format(index, class_, url))
    connection.commit()


if __name__ == '__main__':
    conn = sqlite3.connect('Mzitu.db')
    cursor = conn.cursor()
    start_url = "http://m.mzitu.com/all/"
    base_path = r"H:\爬虫下载文件\Mzitu"

    crawl_infos = get_crawl_urls(start_url)
    pprint(crawl_infos)
    index = 1
    for info in crawl_infos:
        html = get_page(info["href"])
        max_offset = get_max_offset(html)
        # pprint(max_offset)
        for offset in range(1, max_offset + 1):
            html = get_page(info["href"] + "/{}".format(str(offset)))
            img_src = get_image(html)
            store_database(conn, cursor, index, info["dir"], img_src)
            index = index + 1
            print(index, info["dir"], img_src)
            # full_path = base_path + "\\" + info["dir"]
            # if not os.path.exists(full_path):
            #     os.mkdir(full_path)
            # download_image(full_path, "{}.jpg".format(str(offset)), img_src)
    cursor.close()
    conn.close()




