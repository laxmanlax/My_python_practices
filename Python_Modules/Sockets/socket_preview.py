from socket import *
from threading import Thread
import time

port = 5000
host = 'localhost'

def server():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((host,port))
    sock.listen(5)
    while True:
        conn, addr = sock.accept()
        data = conn.recv(1024)
        reply = "server got {}:".format(data)
        conn.send(reply.encode())

def client(name):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    sock.send(name.encode())
    reply = sock.recv(1024)
    sock.close()
    #print "client got {}:".format(reply)

def main():
    sthred = Thread(target=server)
    sthred.daemon = True
    sthred.start()
    count =0
    while True:
        time.sleep(0.9)
        text = "client............."+str(count)
        Thread(target=client, args=(text,)).start()
        count +=1

if __name__=="__main__":
    main()
