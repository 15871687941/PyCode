import scrapy
from liaoxuefeng.items import LiaoxuefengItem
from bs4 import BeautifulSoup

class LiaoxuefengSpider(scrapy.Spider):
    name = 'lxf'
    allowed_domians = ["liaoxuefeng.com", ]

    start_urls = ['https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000', ]

    def parse(self, response):

        soup = BeautifulSoup(response.text.encode(), "lxml")
        as_ = soup.select("#0014316089557264a6b348958f449949df42a6d3a2e542c000 div a")
        print(as_)
        items = []
        for a in as_:
            item = LiaoxuefengItem()
            item["title"] = a.text
            item["link"] = a["href"]
            print(item["title"], item["link"])
            items.append(item)
        return items


# scrapy crawl lxf -o items.json -t json