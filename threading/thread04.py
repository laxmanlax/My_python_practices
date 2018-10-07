#!/usr/bin/env python
import threading
import time


def squre(x):
    print "Calculate square......."
    for i in x:
        time.sleep(0.02)
        print "Square : {}".format(i*i)


def cube(x):
    print "Calculate cube........"
    for j in x:
        time.sleep(0.02)
        print "Cube : {}".format(j*j*j)


def main():
    arr=[2,3,4,5,6]
    t = time.time()
    t1 = threading.Thread(target=squre, args=(arr,))
    t2 = threading.Thread(target=cube, args=(arr,))

    t1.start()
    t2.start()


    t1.join()
    t2.join()


if __name__=="__main__":
    main()
