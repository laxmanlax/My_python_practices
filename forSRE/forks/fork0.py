import os


def child():
    print "Hello this is child process..", os.getpid()
#    os._exit(0)


def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print "This is Parent....", os.getpid(), newpid 

        if raw_input()=="q":
            break

parent()

