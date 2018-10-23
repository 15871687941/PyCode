# encoding = utf-8
import socket
import time

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("127.0.0.1", 2000))
socket.listen(5)
print("Waiting for connection...")
while True:
    socket, address = socket.accept()
    data = socket.recv(1024).decode("utf-8")
    if data == "exit":
        break
    print(address + ":" + data)
    socket.send(data.encode())
socket.close()
