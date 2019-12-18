import time 


def watch(fn):
    fp = open(fn, 'r')

    while True:
        new = fp.readline()

        if new:
            print new,
        else:
            time.sleep(0.5)
        


watch("text", num)

