# encoding = utf-8
# client
from tkinter import *
import socket
import time

main = Tk()
main.title("客户端")
# main.geometry("400x300")
label_A = Label(main, text="IP address:")
label_A.grid(row=0, column=0, sticky=W)
label_B = Label(main, text="Port:")
label_B.grid(row=1, column=0, sticky=W)
enter_A = Entry(main)
enter_A.grid(row=0, column=1, sticky=W)
enter_B = Entry(main)
enter_B.grid(row=1, column=1, sticky=W)


def connect():
    address = enter_A.get()
    port = int(enter_B.get())
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((address, port))
    text_A.insert(END, "正在连接中...")
    text_A.insert(END, "\n" + "连接成功")
    send_info = "\n" + "CLIENT>>>" + "hello!"
    text_A.insert(END, send_info)
    s.send("%s".encode() % send_info)
    while True:
        receive = s.recv(1024).decode()
        if receive != "":
            get_info = "\n" + "SERVER>>>" + receive
            text_A.insert(END, get_info)
            if receive == "exit":
                break

        send_info = enter_C.get()
        send_info = "\n" + "CLIENT>>>" + send_info
        if send_info != "":
            text_A.insert(END, send_info)
            if send_info == "exit":
                break
            s.send(b"%d" % send_info)
        submit(socket)

    s.close()


def submit():
    send_info = enter_C.get()
    send_info = "\n" + "CLIENT>>>" + send_info
    text_A.insert(END, send_info)


button_A = Button(main, text="连接", command=connect)
button_A.grid(row=2, column=0, sticky=W)
button_B = Button(main, text="退出", command=main.quit)
button_B.grid(row=2, column=1, sticky=E)
text_A = Text(main, width=50, height=30)
text_A.grid(row=3)
enter_C = Entry(main)
enter_C.grid(row=4, column=0, sticky=W)


button_C = Button(main, text="提交", command=submit)
button_C.grid(row=4, column=1, sticky=E)

mainloop()
