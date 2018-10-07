# anonymous pipes and threads
import os,time, threading

def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ("Hi..from....child").encode()
        os.write(pipeout, msg)
        zzz = (zzz + 1)%5

def parent(pipein):
    while True:
        line = os.read(pipein, 32)
        print "Parent",os.getpid(),line,"---",time.time()


def main():
    pipein, pipeout = os.pipe()
    threading.Thread(target=child, args=(pipeout,)).start()
    parent(pipein)

if __name__=="__main__":
    main()






