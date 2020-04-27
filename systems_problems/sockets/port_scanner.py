import socket
import time

retry = 5
timeout = 3
delaoy = 3
ip = "google.com"
port = 21001


def is_open(ip, port):
    sock = socket.socket(AF_INET, SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        sock.connect((ip, port))
        sock.shoutdown(sock.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        sock.close()

def check_host(ip, port):
    isup = False
    for i in range(retry):
        if is_open(ip, port):
            isup = True
        else:
            time.sleep(deplay)

    return isup
