#!/usr/bin/env python
from multiprocessing import Pool

def f(n):
    sum = 0
    for x in range(n) :
        sum += x*x
    return sum


def main():
    p = Pool()
    result = p.map(f, range(100))
    print result

if __name__=="__main__":
    main()
