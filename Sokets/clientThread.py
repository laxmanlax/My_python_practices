#!/usr/bin/env python
from socket import *
from threading import Thread 
import time
n=0

def echo_client(addr , n):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(addr)
    
    Thread(target=monitor, args=(n,)).start()

    while True:
        count = "Hello....."+str(n)
        s.send(count.encode)
        resp = s.recv(1024)
        n +=1 
    
    Thread(target=monitor, args=(n,)).start()

def monitor(n):
    while True:
        time.sleep(1)
        print "rqst/sec: {}".format(n)
        n = 0 


echo_client(("127.0.0.1", 25005),n)