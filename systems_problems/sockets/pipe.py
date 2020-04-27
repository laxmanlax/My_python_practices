def child():
    while True:
        msg = "jo"
        os.write(w, msg)



def parent():
    r , w = os.pipe()

    if os.fork() == 0:
        child(w)
    else:
        while True:
            data = os.read(r, 32)
            print data 



import os

def child(w):
    while True:
        msg = "hello"
        os.write(w,msg)

def parent():
    r, w  = os.pipe()

    if os.fork() == 0:
        child(w)
    else:
        while True:
            data = os.read(r,32)
            print data