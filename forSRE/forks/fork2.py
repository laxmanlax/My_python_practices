import os, time


def counter(count):
    for i in range(count):
        time.sleep(1)
        print os.getpid(),'------',i


for i in range(5):
    pid = os.fork()
    if pid == 0:
        counter(i)
        os._exit(0)
    else:
        print "Parent Process......", os.getpid()


print ("Main Process Exiting........")
