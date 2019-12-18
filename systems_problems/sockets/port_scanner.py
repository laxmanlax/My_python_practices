from socket import *

def is_up(ip, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout()

    try:
        s.connect((ip, port))
        s.shutdown(sock.SHUT_RDRT)
        return True
    except:
        return False
    finally:
        s.close()



for i in range(retry):
    if is_up(ip, port):
        return True
    else:
        time.sleep(2)
