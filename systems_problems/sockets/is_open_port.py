import socket
import time

ip = "google.com"
port = 443
retry = 5
delay = 10
timeout = 3

def isOpen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)

    try:
        s.connect((ip, port))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        s.close()


def checkHost(ip, port):
    isup = False
    for i in range(retry):
        if isOpen(ip, port):
            isup = True
        else:
            time.sleep(delay)

    return isup
