#!/usr/bin/env python
from socket import *
from threading import Thread

def echo_server(add):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(add)
    s.listen(5)

    while True:
        client, addr = s.accept()
        print "Connectinon :", addr
        Thread(target=echo_handler, args=(client,)).start()

def echo_handler(client):
    while True:
        data = client.recv(1024).decode()
        print data
        if not data:
            break
        client.send("Hi.....".encode())

echo_server(("127.0.0.1",25005))
