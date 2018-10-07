from socket import * 
from threading import Thread
import time
n = 0 
def echo_client(addr, n):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(addr)

    #message = raw_input()
    #while message.lower().strip()!="bye":
    #    sock.send(message.encode())
    #    data = sock.recv(1024).decode()
    #    print (data)
    #    message = raw_input()

    # while True:
    #     start = time.time()
    #     sock.send(("HI....").encode())
    #     resp = sock.recv(100).decode()
    #     end = time.time()
    #     print resp, end-start

    Thread(target=monitor).start()

    while True:
        sock.send("Hi...").encode()
        resp = sock.recv(200)
        n +=1

    
def monitor(n):
    while True:
        time.sleep(1)
        print (n , "reqs/sec")
        n = 0 

echo_client(("127.0.0.1", 25002), n)
