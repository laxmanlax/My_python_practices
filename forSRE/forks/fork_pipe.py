import os
import time

def child(w):
    pid = os.getpid()
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ("This is the child pid ====" + str(pid)+ "").encode()
        os.write(w,msg)
        zzz = (zzz+1)%5 


def parent():
    read_from , write_to = os.pipe()

    if os.fork() == 0:
        child(write_to)
    else:
        while True:
          line = os.read(read_from, 100)
          print "Parent =====>>>", os.getpid(), line


parent() 
