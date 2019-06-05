#!/usr/bin/env python
# 有问题 先存着
from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH, ThreadingMixIn as TMI)
from time import ctime

HOST = ''
PORT = 12346
ADDR = (HOST, PORT)


class Server(TMI, TCP):
    pass


class MyRequestHandler(SRH):
    def handle(self):
        print '...connected from:', self.client_address
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))


tcpServ = Server(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()
