#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 有问题 先存着
from socket import *

HOST = 'localhost'
PORT = 12346
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = raw_input('>')
    if not data:
        break
    tcpCliSock.send('%s\r\n' % data)
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print data
    tcpCliSock.close()
