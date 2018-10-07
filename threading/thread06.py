#!/usr/bin/env python
import Queue
import threading
import multiprocessing

def worker(q, val, j):
    for i  in val:
        q.put(j**2)

def main():
    q = Queue.Queue()

    cups = multiprocessing.cpu_count()
    for i in range(3):
        t1 = threading.Thread(target=worker, args=(q,range(5), i))
        t1.start()

    while not q.empty():
        print q.get()


if __name__=="__main__":
    main()
