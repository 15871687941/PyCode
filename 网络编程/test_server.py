# encoding = utf-8
from tkinter import *
import socket
import time
# from multiprocessing import Process
from threading import Thread, Lock
# 连接服务器
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 2000))
sock.listen(1)
# lock = Lock()
msg = []
# socket, address = sock.accept()

# 函数
def submit(msg):
    # lock.acquire()
    # global msg
    get_msg = enter_input.get()
    msg.append(get_msg)
    # print(msg)
    # lock.release()
    enter_input.delete(0, END)
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    show_msg = "我({}):\n>>>{}\n".format(date, get_msg)
    print(show_msg)
    text_mutual.insert(END, show_msg)
    # text_mutual.update()


# 交互
def receive_msg(sock, msg):
    s, address = sock.accept()
    print(address)
    # sock, address = sock.accept()
    while True:
        # lock.acquire()
        # global msg
        if len(msg) != 0:
            s.send((msg.pop()).encode())
            # msg = ""
        # lock.release()
        while True:
            receive = s.recv(1024).decode()
            time.sleep(1)
            if receive:
                if receive == "exit":
                    root.quit()
                date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                play_msg = "客户端({}):\n>>>{}\n".format(date, receive)
                text_mutual.insert(END, play_msg)
                text_mutual.update()
            else:
                break
    s.close()
    sock.close()


root = Tk()
root.title("聊天室（服务端）")
# 界面
text_mutual = Text(root, width=60, height=30)
text_mutual.grid(row=0, column=0, columnspan=2)
enter_input = Entry(root, width=50)
enter_input.grid(row=1, column=0)
button_submit = Button(root, text="提交", width=9, command=lambda: submit(msg))
# button_submit.bind_all("<Enter>", submit)
button_submit.grid(row=1, column=1)
text_free = Text(root, width=30, height=32, bg="green")
text_free.grid(row=0, column=2, rowspan=2)
# process_send = Process(target=receive_msg)
thread_send = Thread(name="receiveMsg", target=receive_msg, args=(socket, msg))
# thread_main = Thread(name="mainloop", target=mainloop)
# process_send.start()
thread_send.start()
# thread_send.join()
# time.sleep(1)
root.mainloop()
# thread_main.start()
