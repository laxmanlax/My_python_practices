import os, time
def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ("HI...from Child....").encode()
        os.write(pipeout, msg)
        zzz = (zzz + 1)%5

def parent():
    pipein, pipeout = os.pipe()
    if os.fork() == 0:
        child(pipeout)
    else:
        os.close(pipeout)
        while True:
            line = os.read(pipein, 32)
            print "Parent", os.getpid(),line,"---",time.time()


parent()
