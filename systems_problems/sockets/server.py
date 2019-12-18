from socket import *
HOST = '127.0.0.1'
PORT =21101

conn = socket(AF_INET, SOCK_STREAM)
conn.bind((HOST,PORT))
conn.listen(2)

c_conn, addr = conn.accept()

while True:
    data = c_conn.recv(1024).decode()
    if not data:
        break

    c_conn.send(data.encode())
