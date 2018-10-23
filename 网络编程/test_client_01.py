# encoding = utf-8
import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 2222))

while True:
    send_msg = input("（客户端）请输入要发送的消息：")
    sock.send(send_msg.encode())
    time.sleep(2)
    receive_msg = sock.recv(1024).decode()
    if receive_msg:
        print("（客户端）这是收到的信息：{}".format(receive_msg))
sock.close()
