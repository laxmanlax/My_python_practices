import os
import time

def child(w):
    zzz = 0
    while True:
        time.sleep(0.0002)
        msg = "This is child.."
        #wrt = os.fdopen(w, "w")
        os.write(w,msg)
        os.close(w)        
        zzz = (zzz + 1) %5 

def parent():
    read_from , write_to  = os.pipe()
    if os.fork()==0:
        os.close(read_from)
        child(write_to)
    else:
        os.close(write_to)
        pipein = os.fdopen(read_from,'r')
        while True:
            time.sleep(2)
            line = pipein.read()
            print "Parent {} got {} at {}".format(os.getpid(), line , time.time())


parent()

