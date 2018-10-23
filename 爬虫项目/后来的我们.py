import jieba
import requests
from wordcloud import WordCloud
import time
from bs4 import BeautifulSoup
from pprint import pprint
import pymongo
import matplotlib.pyplot as plt
import  numpy as np

def login(login_url):
    data = {
        "source": "index_nav",
        "form_email": "15871687941",
        "form_password": "asd2743075"
    }
    session = requests.Session()
    session.post(login_url, data=data)
    return session


def get_page(session, url):
    response = session.get(url)
    if response.status_code == 200:
        html_code = response.text
        return html_code
    else:
        return "%s Error" % url


def parse_page(html_code):
    soup = BeautifulSoup(html_code, "lxml")
    comments = soup.select("div#comments div.comment-item")
    data = list()
    for comment in comments:
        result = dict()
        result["name"] = comment.select(".comment-info a")[0].text.strip()
        result["vote"] = comment.select(".votes")[0].text.strip()
        result["content"] = comment.select(".short")[0].text.strip()
        data.append(result)
    return data


def store_database(datas):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    my_database = client["movie"]
    my_collection = my_database["next_us"]
    my_collection.insert(datas)
    print("存储成功！")
    client.close()


def data_show(datas):
    votes = []
    values = []
    for data in datas:
        votes.append(int(data["vote"]))
    max_vote = max(votes)
    for vote in range(0, max_vote + 1):
        values.append(votes.count(vote))
    print(values)
    # plt.figure()
    # plt.plot([i for i in range(0, max_vote + 1)], values, color='red')
    # plt.xlabel("Counts")
    # plt.ylabel("Values")
    # # plt.xticks([i for i in range(0, 401, 100)])
    # plt.yticks([i for i in range(0, 3001, 500)])
    # plt.show()


def word_cloud(datas):
    text = []
    for data in datas:
        text.append(data["content"])
    text = ''.join(text)
    cut_text = jieba.cut(text)
    result = '/'.join(cut_text)

    wc = WordCloud(font_path="C:\\Windows\\Fonts\\SIMLI.ttf",
                   background_color="white",
                   width=800,
                   height=600,
                   max_words=2000,
                   margin=5,
                   max_font_size=80,
                   random_state=40,
                   )
    mword = wc.generate(result)
    plt.figure("后来的我们")
    plt.imshow(mword)
    plt.axis("off")
    plt.show()



if __name__ == '__main__':
    login_url = "https://www.douban.com/accounts/login"
    session = login(login_url)
    base_url = "https://movie.douban.com/subject/26683723/comments?start={}&limit=20&sort=new_score&status=P"
    offset = 0
    datas = list()
    while offset <= 480:
        html_code = get_page(session, base_url.format(str(offset)))
        # print(html_code)
        # time.sleep(20)
        data = parse_page(html_code)
        print(data)
        datas.extend(data)
        print(len(datas))
        offset += 20
    word_cloud(datas)
    # pprint(datas)
    # data_show(datas)
    # store_database(datas)
    # pprint(datas)
