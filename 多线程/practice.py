import threading, requests

local_school = threading.local()


def crawl_url():
    url = local_school.url
    response = requests.get(url)
    print(response.text)


def transfer_url(url):
    local_school.url = url
    crawl_url()