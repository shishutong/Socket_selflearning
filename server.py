# -*- coding:utf-8 -*-
import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_port = (socket.gethostname(), 8888)
sk.bind(ip_port)
sk.listen(5)

while True:
    clientserver, addr = sk.accept()
    print("ip is : ", addr)
    msg = "hello, world!"
    clientserver.send(msg.encode())
    clientserver.close()