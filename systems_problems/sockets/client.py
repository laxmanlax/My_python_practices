from socket import *
HOST = '127.0.0.1'
PORT = 21101

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST,PORT))

message = raw_input()

while message.lower().strip()!="bye":
    s.send(message.encode())
    data = s.recv(1024).decode()
    print data
    message = raw_input()
