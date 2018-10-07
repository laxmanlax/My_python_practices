#!/usr/bin/env python
import multiprocessing
import time 

def claculate_Square(nums):
    for n in nums:
        time.sleep(0.05)
        print "Square : {}".format(n*n)


def calculate_Cube(nums):
    for n in nums:
        time.sleep(0.05)
        print "Cube :{}".format(n*n*n)


def main():
    arr = [3,4,5,6,7,8]
    p1 = multiprocessing.Process(target=claculate_Square, args=(arr,))
    p2 = multiprocessing.Process(target=calculate_Cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__=="__main__":
    main()