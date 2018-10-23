import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup
import re
from zhaoxiaoshuo.items import ZhaoxiaoshuoItem


class ZhaoXiaoShuo(scrapy.Spider):
    name = "zhaoxiaoshuo"
    allowed_domains = ['zhaoxiaoshuo.com']
    first_url = 'http://www.zhaoxiaoshuo.com'
    base_url = 'http://www.zhaoxiaoshuo.com/all.php?c={}&o=0&s=0&f=2&l=0&page=1'

    def start_requests(self):
        for i in range(2, 22):
            url = self.base_url.format(str(i))
            yield Request(url, self.get_max_page, meta={
                'url': url
            })
        yield Request(self.base_url.format(str(0)), self.get_max_page, meta={
            'url': self.base_url.format(str(0))
        })

    def get_max_page(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        max_page = int(re.search("\d+", soup.select(".pages a")[4].text).group())
        url = response.meta['url']
        for page in range(1, max_page + 1):
            url = url.replace("page=1", "page={}".format(str(page)))
            yield Request(url, self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        ul = soup.select(".clearfix")[2]
        lis = ul.select("li")
        for li in lis:
            # category = li.select(".width369")[0].text.strip()
            name = li.select(".green")[0].text.strip()
            status = li.select(".red")[0].text.strip()
            author = li.select(".width111")[0].text.strip()
            url = self.first_url + li.select(".green")[0]['href']
            yield Request(url, self.get_information, meta={
                # 'category': category,
                'name': name,
                'status': status,
                'author': author
            })

    def get_information(self, response):
        item = ZhaoxiaoshuoItem()
        soup = BeautifulSoup(response.text, "lxml")
        item['book_category'] = soup.select(".crumbswrap a")[1].text.strip()
        item['book_name'] = response.meta['name']
        item['book_author'] = response.meta['author']
        item['book_words'] = soup.select(".r420 p span")[1].text.strip()
        item['book_vote'] = soup.select(".r420 p span")[2].text.strip()
        item['book_collection'] = soup.select(".r420 p span")[2].text.strip()
        item['book_status'] = response.meta['status']
        return item













