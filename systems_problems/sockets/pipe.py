



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