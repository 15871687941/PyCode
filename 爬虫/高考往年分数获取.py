# coding = utf-8
# 2015年湖北省高校录取分数详情
import requests
# from lxml import etree
from bs4 import BeautifulSoup
import pandas
source_url = "http://kaoshi.edu.sina.com.c\
n/college/scorelist?tab=&majorid=&wl=&loca\
l=13&provid=13&batch=&syear=2015&page={}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit\
    /537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    "Host": "kaoshi.edu.sina.com.cn"
}
hubei = {}
university = []
maxscore = []
averagescore =[]
location = []
class_ = []
count = []
year = []
for page in range(1, 18):
    response = requests.get(source_url.format(page))
    if response.encoding != "utf-8":
        response.encoding = "utf-8"
    # print(response.text)
    # html = etree.HTML(response.text)
    # print(html)
    # trs = html.xpath('//*[@id="score"]/div[2]/table/tbody/tr')
    soup = BeautifulSoup(response.text, "lxml")
    trs = soup.select(".tbL2 tr")
    for i in range(1, len(trs)):
        university.append(trs[i].select("td")[0].text)
        location.append(trs[i].select("td")[1].text)
        class_.append(trs[i].select("td")[2].text)
        count.append(trs[i].select("td")[3].text)
        year.append(trs[i].select("td")[4].text)
        maxscore.append(trs[i].select("td")[5].text)
        averagescore.append(trs[i].select("td")[6].text)

hubei['院校名称'] = university
hubei['考生所在地'] = location
hubei['考生类别'] = class_
hubei['批次'] = count
hubei['年份'] = year
hubei['最高分'] = maxscore
hubei['平均分'] = averagescore
print(hubei)
pd = pandas.DataFrame(hubei)
pd.to_excel("C:\\Users\\God\\Desktop\\湖北.xlsx")
