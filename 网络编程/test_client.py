# encoding = utf-8
from tkinter import *
import socket
import time
from threading import Thread, Lock
from multiprocessing import Process
# 连接服务器
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 2000))
msg = []
# lock = Lock()


# 函数
def submit(msg):
    # lock.acquire()
    # global msg
    get_msg = enter_input.get()
    msg.append(get_msg)
    # lock.release()
    enter_input.delete(0, END)
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    show_msg = "我({}):\n>>>{}\n".format(date, get_msg)
    text_mutual.insert(END, show_msg)
    text_mutual.update()


def receive_msg(sock, msg):
    # global msg
    while True:
        # lock.acquire()
        if len(msg) != 0:
            sock.send((msg.pop()).encode())
            # msg = []
        # lock.release()
        receive = sock.recv(1024).decode()
        time.sleep(1)
        print(receive)
        if len(receive) != 0:
            if receive == "exit":
                root.quit()
            date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            play_msg = "服务端({}):\n>>>{}\n".format(date, receive)
            text_mutual.insert(END, play_msg)
    sock.close()


root = Tk()
root.title("聊天室(客户端)")
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

thread_send = Thread(name="receiveMsg", target=receive_msg, args=(sock, msg))
# process_send = Process(target=receive_msg)
# process_send.start()
# process_send.run()
# thread_send.start()
thread_send.start()
# thread_send.join()
# time.sleep(1)
root.mainloop()
