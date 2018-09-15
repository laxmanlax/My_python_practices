from socket import *
from threading import Thread

def echo_server(addr):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print "Connection :", addr 
        Thread(target=echo_handler, args=(client,),).start()
        #echo_handler(client)


def echo_handler(client):
    while True:
        req = client.recv(1024)
        if not req:
            break 
        resp = str(req).encode()
        client.send(resp)
    print "Closed"


#def fib(n):
#    if n <=2 :
#        return 1 
#    else:
#        return fib(n-1) + fib(n-2)

echo_server(("127.0.0.1", 25002))

