# coding = UTF-8
from tkinter import *
import requests, re
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
window = Tk()
window.title("网易云音乐")
window.geometry("550x400+400+180")
label1 = Label(window, text="请输入要下载的歌单URL:", font=("楷书", 15))
label1.grid(row=0, column=0)

enter1 = Entry(window, font=("微软雅黑", 20))
enter1.grid(row=0, column=1)

text = Listbox(window, font=("微软雅黑", 15), width=45, height=10)
text.grid(row=1, columnspan=2)


def get_music_info(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",
        "Host": "music.163.com"
    }
    response = requests.get(url, headers=headers)
    # params=H3ALUIUwx4FOb3YoAXXDQ1E0u41l0A25PeSnxfVhmj0UMqvUS2RNWgT%2FhP5nRD8cJyXb7VrtrROh%2BezbHT5zXhGng%2BMcrapDkv9ihhPuiXG2BsiETTKsZwINNAkSeiou&
    # encSecKey=5f1265d2f667a06b34c2afa7e8552ed60c99599b973fb44b7cace059c2c107c0511ba5be297d247c4d333b9b4fd0cd538d6b36e759171b6f76e39c4e5d6c281ae17d904c87c9e7910690e2c33c3b30ad3e5d668b8b9db360489d968eff9b6f44e0b192b38f0f93a527fddf5b5af1e81dc7384bd0f39a4c2c29192da3d2c3faaa
    result = response.content.decode()
    soup = BeautifulSoup(result, "lxml")
    songs = []
    urlretrieve("http://music.163.com/#/song?id=409031749", r"C:\Users\God\Desktop\1.mp3")
    for link in soup.select("div.f-hide ul li a"):
        song = {}
        song['name'] = link.text
        song['id'] = "".join(re.findall("[0-9]+", link['href']))
        songs.append(song)
    return songs


def download_musics():
    url = enter1.get()
    songs = get_music_info(url)
    for song in songs:
        text.insert(END, song["name"]+": "+song["id"])
        text.see(END)
        text.update()



button1 = Button(window, text="开始下载", font=("微软雅黑", 15), command=download_musics)
button1.grid(row=2, column=0, sticky=W)

button2 = Button(window, text="退出", font=("微软雅黑", 15), command=window.quit)
button2.grid(row=2, column=1, sticky=E)

window.mainloop()