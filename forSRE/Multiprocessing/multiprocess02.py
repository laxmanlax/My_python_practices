#!/usr/bin/env python
import multiprocessing
import time 

result_all = []

def claculate_Square(nums):
    for n in nums:
        time.sleep(0.05)
        print "Square : {}".format(n*n)
        result_all.append(n*n)
    print "Inside Process p1: {}".format(result_all)

def calculate_Cube(nums):
    for n in nums:
        time.sleep(0.05)
        print "Cube :{}".format(n*n*n)


def main():
    arr = [3,4,5,6,7,8]
    p1 = multiprocessing.Process(target=claculate_Square, args=(arr,))
    p1.start()
    p1.join()
    print "Outsie process P1: {}", format(result_all)

if __name__=="__main__":
    main()