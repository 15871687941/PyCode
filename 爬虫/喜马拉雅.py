# coding = UTF-8
import requests, json, os


class XiMa(object):
    def __init__(self, book_name, id):
        self.__book_name = book_name
        self.__id = id

        self.__headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; W\
            OW64) AppleWebKit/537.36 (KHTML, like Gecko) C\
            hrome/65.0.3325.146 Safari/537.36"
        }
        # self.__start_url = "https://www.ximalaya.com/revision/play/album?albumId={}&pageNum={}&pageSize=30"
        self.__start_url = "https://www.ximalaya.com/revision/play/album?albumId=" + self.__id + "&pageNum={}&pageSize=30"
        self.__book_url = []
        for i in range(1, 10):
            self.__book_url.append(self.__start_url.format(i))

        self.__audio_list = []

    def get_book_msg(self):
        for url in self.__book_url:
            response = requests.get(url, headers=self.__headers)
            result = response.content.decode()
            msg_dict = json.loads(result)
            for data in msg_dict['data']['tracksAudioPlay']:
                list = {}
                list['name'] = data['trackName']
                list['src'] = data['src']
                list['index'] = data['index']
                self.__audio_list.append(list)

    def save(self):
        if not os.path.exists(r"H:\爬虫下载文件\喜马拉雅\{}".format(self.__book_name)):
            os.mkdir(r"H:\爬虫下载文件\喜马拉雅\{}".format(self.__book_name))
        for i in self.__audio_list:
            print("正在爬取第%d个音频..." % (self.__audio_list.index(i) + 1))
            with open(r"H:\爬虫下载文件\喜马拉雅\{}\{}、{}.m4a".format(self.__book_name, i['index'], i['name']), "wb") as fp:
                response = requests.get(i['src'], headers=self.__headers)
                fp.write(response.content)
                print("第%d个音频爬取成功" % (self.__audio_list.index(i) + 1))

    def run(self):
        self.get_book_msg()
        self.save()


if __name__ == '__main__':
    # import 喜马拉雅_情感故事ID.ID
    # for id in ids:
    #     XiMa(id['book_name'], id['id']).run()
    xima = XiMa("南城故事")
    xima.run()