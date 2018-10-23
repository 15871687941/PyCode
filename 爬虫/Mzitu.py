from bs4 import BeautifulSoup
import requests
import os

start_url = 'http://www.mzitu.com/all'
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Mobile Safari/537.36"
}
response = requests.get(start_url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
urls = soup.select(".url a")
# print(urls)
for url in urls:
    print(url)
    title = url.text
    path = "H:\\爬虫下载文件\\{}".format(title)
    if not os.path.exists(path):
        os.mkdir(path)
    link = url['href']
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'lxml')
    max_page = int(soup.select(".pagenavi a span")[-2].text)
    for i in range(1, max_page + 1):
        link = link + "/{}".format(str(i))
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'lxml')
        file_name = soup.select("title")[0].text
        print(file_name)
        img_url = soup.select(".main-image p a img")[0]['src']
        response = requests.get(img_url)
        with open(path + "\\{}.jpg".format(file_name), "ab") as fp:
            print("正在下载({})文件夹下的第{}个文件".format(path, str(i)))
            fp.write(response.content)
            print("下载成功")

