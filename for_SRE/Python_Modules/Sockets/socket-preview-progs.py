import sys, os, time
from threading import Thread
from socket import *

port = 50006
host = "localhost"

def server():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((host,port))
    sock.listen(600)
    while True:
        conn, addr = sock.accept()
        data = conn.recv(1024)
        reply = 'server got: {}'.format(data)
        conn.send(reply.encode())

def client(name):
    time.sleep(0.7)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    sock.send(name.encode())
    reply = sock.recv(1024)
    sock.close()
    print "client got:{}".format(reply)

def main():
    mode = int(sys.argv[1])
    if mode == 1:
        server()
    elif  mode == 2:
        client("client:process=%s" %os.getpid())
    else:
        for i in range(100):
            client1 = 'client:thread='+str(1)
            Thread(target=client, args=(client1,)).start()
    
if __name__=="__main__":
    main()




