
def child(w):
    while True:
        msg = "fff"
        os.write(w, msg)


def parent():
    r, w = os.pipe()

    if os.fork() == 0:
        child(w)
    else:
        data = os.read(r, 32)
        print data
