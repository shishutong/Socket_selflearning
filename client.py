# -*-coding:utf-8 -*-
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostname()
port = 8888
s.connect((ip, port))

msg = s.recv(1024)
s.close()
print("msg: ",msg)