# -*- coding:utf-8 -*-

import socket
import threading
import time


# 具体的方法，用于多线程
def tcplink(clientsocket, addr):
    print "start new threading from %s:%s" % addr
    msg = "Welcome!"
    clientsocket.send(msg)
    while True:
        data = clientsocket.recv(1024)
        time.sleep(5)
        if not data or data.decode('utf-8') == "quit":
            break
        clientsocket.send("Hello, %s" % data.decode("utf-8").encode("utf-8"))
    clientsocket.close()
    print "%s:%s threading is close" % addr


# 建立实例
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ip, 端口
# 端口号大于1024
ip_port = ("127.0.0.1", 12345)
# 绑定
ServerSocket.bind(ip_port)
# 建立监听，一般是5就行
print "wait the connect...."
ServerSocket.listen(5)
# 一直循环，持续运行
while True:
    ClientSocket, Addr = ServerSocket.accept()
    t = threading.Thread(target=tcplink, args=(ClientSocket, Addr))
    t.start()
