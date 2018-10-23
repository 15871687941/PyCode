# coding = UTF-8
import requests, re
from bs4 import BeautifulSoup


class ID(object):
    def __init__(self):
        self.start_url = "https://www.ximalaya.com/qinggan/p{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",
            "Host": "www.ximalaya.com"
        }
        self.urls = []
        for i in range(1, 35):
            self.urls = self.start_url.format(i)
        self.ids = []

    def get_id(self):
        for url in self.urls:
            response = requests.get(url, headers=self.headers)
            result = response.content.decode()
            soup = BeautifulSoup(result, "lxml")
            lis = soup.select(".content ul li")
            for li in lis:
                id_dict = {}
                book_name = li.select(".album-title")[0]['title']
                link = li.select(".album-title")[0]["href"]
                id = ''.join(re.findall("/([0-9]+)/$", link))
                id_dict['book_name'] = book_name
                id_dict['id'] = id
                self.ids.append(id_dict)

    def run(self):
        self.get_id()
        return self.ids


