#/usr/bin/env python 
import socket

HOST = '127.0.0.1'
PORT = 25002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

message = raw_input()

while message.lower().strip()!="bye":
    s.send(message.encode())
    data = s.recv(1024).decode()
    print  data
    message = raw_input()




