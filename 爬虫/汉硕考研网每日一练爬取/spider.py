# encoding = utf-8
import requests
from urllib.parse import urlencode

# ?token=407388703&lang=zh_CN&f=json&ajax=1&action=list_ex&begin=25&count=5&query=&fakeid=MzI5MjQxOTk3Mg%3D%3D&type=9"
class Spider(object):
    def __init__(self):
        self.start_url = "https://mp.weixin.qq.com/cgi-bin/appmsg?token=407388703&lang=zh_CN&f=json&ajax=1&action=list_ex&begin={}&count=5&query=&fakeid=MzI5MjQxOTk3Mg%3D%3D&type=9"
        self.param_changeable = 0
        self.available_urls = {}

    def get_available_urls(self):
        while True:
            full_url = self.start_url.format(str(self.param_changeable))
            response = requests.get(full_url)
            data_json = response.json()
            app_msg_list = data_json["app_msg_list"]
            if len(app_msg_list) == 0:
                break
            else:
                for url in app_msg_list:
                    if "汉硕真题及答案" in url["title"]:
                        self.available_urls[url["title"]] = url["link"]
        print(self.available_urls)


if __name__ == '__main__':
    spider = Spider()
    spider.get_available_urls()
