# coding: utf-8
import requests
from bs4 import BeautifulSoup
import pandas

source_url = "http://music.guqu.net/ShowNew.asp?page={}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) Appl\
    eWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",
    "Host": "music.guqu.net"
}
musics = dict()
name = list()
title = list()
shower = list()

def get_page(page):
    url = source_url.format(page)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = "gbk"
        print(response.text)
        return response.text
    else:
        return None

def parse_page(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    trs = soup.select("")
    for tr in trs:
        name.append(tr.select("td")[0].select("a")[0].text())
        print(name)
        title.append(tr.select("td")[0].select("a")[1].text())
        print(title)
        shower.append(tr.select("td")[0].text())
        print(shower)

def store_page():
    print(name, title, shower)
    musics['name'] = name
    musics['title'] = title
    musics['shower'] = shower
    pd = pandas.DataFrame(musics)
    pd.to_csv("C:\\Users\\God\\Desktop\\古曲.csv")


if __name__ == "__main__":
    for page in range(1, 2):
        result = get_page(page)
        parse_page(result)
    print(musics)
    store_page()




