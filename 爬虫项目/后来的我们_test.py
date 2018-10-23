# coding = utf-8
# import requests
# from bs4 import BeautifulSoup
# from pprint import pprint
# url = "https://movie.douban.com/subject/2\
# 6683723/comments?start=0&limit=20&sort=new_sco\
# re&status=P"
# response = requests.get(url)
# html_code = response.text
# soup = BeautifulSoup(html_code, "lxml")
# comments = soup.select("div#comments div.comment-item")
# pprint(comments)
# data = list()
# for comment in comments:
#     result = dict()
#     result["name"] = comment.select("span.comment-info a")[0].text.strip()
#     result["vote"] = comment.select(".votes")[0].text.strip()
#     result["content"] = comment.select(".short")[0].text.strip()
#     print(result)
import matplotlib.pyplot as plt
import jieba
import chardet
from wordcloud import WordCloud
# 1、打开文本
with open(r"C:\Users\God\Desktop\考研计划.txt", 'rb') as fp:
    text = fp.read()
print(text.decode("GB2312"))
type_ = chardet.detect(text)
print(type_)
# 2、结巴分词
# cut_text = jieba.cut(text)
# result = '/'.join(cut_text)
# # print(result)
# # 3、生成词云图
# wc = WordCloud(background_color="white",
#                max_words=2000,
#                margin=5,
#                font_path="C:\\Windows\\Fonts\\SIMLI.ttf",
#                random_state=40,
#                width=800,
#                height=600,
#                )
# mword = wc.generate(result)
# print(type(mword))
# plt.figure("词云图")
# plt.imshow(mword)
# plt.axis("off")  # 关闭图像坐标系
# plt.show()

