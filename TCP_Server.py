#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import *
from time import ctime

Host = gethostname()
port = 9999
BuffSize = 1024
Addr = (Host, port)

TcpSerSocket = socket(AF_INET, SOCK_STREAM)
TcpSerSocket.bind(Addr)
TcpSerSocket.listen(5)

while True:
    print "Waiting the connecting ......"
    TcpClientSocket, Address = TcpSerSocket.accept()
    print "... connect from : ", Address

    while True:
        data = TcpClientSocket.recv(BuffSize)
        if not data:
            break
        TcpClientSocket.send("[%s] %s" % (ctime(), data))
        print [ctime()], ':', data

TcpClientSocket.close()
TcpSerSocket.close()
