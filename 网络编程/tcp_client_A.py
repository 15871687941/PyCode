# encoding = utf-8
import socket
import time
# 1、连接前的准备工作，建立套接字，打开网络连接
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 指定网络协议和流
# 2、连接
socket.connect(("127.0.0.1", 2000)) # 指定连接的IP地址和端口号
# 3、发送消息
while True:
    inp = input("输入要发送的信息：")
    socket.send(inp.encode())
    time.sleep(2)
    ret = socket.recv(1024).decode("utf-8")
    if ret == "exit":
        break
    print(ret)
socket.close()

