# -*- coding:utf-8 -*-

import socket


ip_port = ("127.0.0.1", 12345)
ClientServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientServer.connect(ip_port)
data = ClientServer.recv(1024)
print "msg: %s" % data
datalist = ["chengdong", "lele", "xiaojie"]
for d in datalist:
    ClientServer.send(d)
    data = ClientServer.recv(1024)
    print data
print "ClientServer close!"
ClientServer.close()


