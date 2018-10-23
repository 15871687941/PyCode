import requests, sys, re, time, json
from bs4 import BeautifulSoup
# non_bmp_map=dict.fromkeys(range(0x10000,sys.maxunicode+1),0xfffd)
headers={'Host': 'maoyan.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}


def get_one_page(url):
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.content.decode()
    # .translate(non_bmp_map)
    return None


def parse_one_page(html):
    soup = BeautifulSoup(html, "lxml")
    dds = soup.select("dl.board-wrapper dd")
    for dd in dds:
        item = dict()
        item["index"] = dd.select("i.board-index")[0].text
        item["image"] = dd.select("img.board-img")[0].attrs["data-src"]
        item["title"] = dd.select("p.name a")[0].text
        item["actor"] = dd.select("p.star")[0].text.strip()
        item["time"] = dd.select("p.releasetime")[0].text
        item["score"] = dd.select("p.score")[0].text
        yield item

    # pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?board-image.*?'
    #                    +'src="(.*?)">.*?title=.*?>(.*?)</a>.*?class="star"'
    #                    +'>(.*?)</p>.*?class="releasetime">(.*?)</p>.*?class'
    #                    +'="integer">(.*?)</i>.*?class="fraction">(.*?)</i>.*?'
    #                    +'</dd>')
    # items = re.findall(pattern,html)
    # for item in items:
    #     yield{
    #         'index': item[0],
    #         'image': item[1],
    #         'title': item[2],
    #         'actor': item[3],
    #         'time': item[4],
    #         'score': item[5]+item[6]
    #         }


def write_to_file(content):
    with open(r'C:\Users\God\Desktop\result.txt','w',encoding='utf-8') as file:
        file.write(json.dumps(content,ensure_ascii=False)+'\n')

    
def main(offset):
    url = "http://maoyan.com/board/4?offset="+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__=='__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)
