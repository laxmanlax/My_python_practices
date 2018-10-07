import os

def child():
    return "I am the child....", os.getpid()

def parent():
    return "I am the parent...", os.getpid()


pid = os.fork()

if pid == 0: 
    print child()
else:
    print parent()

