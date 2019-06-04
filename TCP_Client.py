#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import *

BuffSize = 1024
host = gethostname()
port = 9999
Addr = (host, port)
TcpCliSocket = socket(AF_INET, SOCK_STREAM)
TcpCliSocket.connect(Addr)

while True:
    data = raw_input(">")
    TcpCliSocket.send(data)
    data = TcpCliSocket.recv(BuffSize)
    if not data:
        break
    print data
