from socket import *
from fib import fib
#from threading import Thread

def fib_server():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('127.0.0.1', 12101))
    sock.listen(5)

    while True:
        client, addr = sock.accept()
        print ("Connection ", addr)
        fib_handler(client)
        #Thread(target=echo_handler, args=(client,)).start()

def fib_handler(client):
    while True:
        data = client.recv(1024).decode()
        print "Request to calaute fib of ",data,"\n"
        if not data:
            break

        n = int(data)
        result = fib(n)
        resp = str(result)+"\n"
        client.send(resp.encode())


fib_server()
