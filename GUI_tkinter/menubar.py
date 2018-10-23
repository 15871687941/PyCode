# coding = UTF-8
from tkinter import *

windows = Tk()
windows.title("SCALE")
windows.geometry("200x200")

label = Label(windows, text="", bg="yellow")
label.pack()

counter = 0
def do_job():
    global counter
    label.config(text="do " + str(counter))
    counter += 1


menubar = Menu(windows, bg="black")
# tearoff值为1时，菜单可以独立出来，值为0时，不可以。
filemenu = Menu(menubar, tearoff=1)
menubar.add_cascade(label="文件", menu=filemenu)
filemenu.add_command(label="新建", command=do_job)
filemenu.add_command(label="打开", command=do_job)
filemenu.add_command(label="保存", command=do_job)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=windows.quit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)

windows.config(menu=menubar)
windows.mainloop()