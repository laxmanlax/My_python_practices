#!/usr/bin/env python
from socket import *

HOST  = '127.0.0.1'
PORT  = 25002

server = (HOST, PORT)
s = socket(AF_INET, SOCK_STREAM)
s.bind(server)
s.listen(2)


print "Connected to address..............{}".format(addr)
while True:
    conn , addr = s.accept()
    data = conn.recv(1024)
    if not data:
        break

    data = "Accepted" + data
    conn.send(data)
