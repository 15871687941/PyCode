import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 2222))
sock.listen(2)
# sock, address = sock.accept()

while True:
    sock, address = sock.accept()
    print(address)
    receive_msg = sock.recv(1024).decode()
    if receive_msg:
        print("（服务器端）这是收到的消息：{}".format(receive_msg))
    send_msg = input("（服务器端）请输入要发送的下消息：")
    sock.send(send_msg.encode())
sock.close()
