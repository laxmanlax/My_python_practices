#!/usr/bin/env python 
from socket import *


server =("127.0.0.1", 25002)
s = socket(AF_INET, SOCK_STREAM)
s.bind(server)
s.listen(2)
conn , addr = s.accept()

print "Connected to address..............{}".format(addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data)
