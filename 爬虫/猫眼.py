import threading, requests, time
from bs4 import BeautifulSoup
class MaoYanThread(threading.Thread,):
    def __init__(self, threadID, name, urls):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.urls = urls

    def run(self):
        print("Strating " + self.name)
        # threadLock.acquire()
        crawl_maoyan(self.urls)
        # threadLock.release()
        print("Exiting " + self.name)

def crawl_maoyan(urls):
    threadLock.acquire()
    url = urls.pop()
    print(urls)
    threadLock.release()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WO\
        W64) AppleWebKit/537.36 (KHTML, like Gecko) Chr\
        ome/55.0.2883.87 Safari/537.36",
        "Host": "maoyan.com"
    }
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    dds = soup.select(".board-wrapper dd")
    for dd in dds:
        index = dd.select(".board-index")[0].text
        name = dd.select(".name a")[0].text
        star = dd.select(".star")[0].text
        releasetime = dd.select(".releasetime")[0].text
        print(index, name, star, releasetime)
        time.sleep(2)

threadLock = threading.Lock()
threads = list()
base_url = "http://maoyan.com/board/4?offset={}"
urls = list()
names = list()
IDs = list()
for offset in range(9, -1, -1):
    url = base_url.format(offset*10)
    urls.append(url)
    name = "Thread-{}".format(offset+1)
    names.append(name)
    IDs.append(offset+1)

for name in names:
    threads.append(MaoYanThread(IDs.pop(), name, urls))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
# t1 = MaoYanThread(1, "Thread-1", urls=urls)
# t2 = MaoYanThread(2, "Thread-2", urls=urls)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

