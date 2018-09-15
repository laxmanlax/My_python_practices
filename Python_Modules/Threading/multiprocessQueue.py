import math 
import random
from multiprocessing import Process, Queue
from os import getpid

def is_even(n):
    if n%2==0:
        return True
    return False

def Process_main(q):
    while True:
        n = q.get()
        if n == 0:
            return True 
        if is_even(n):
            print n 
    

if __name__=="__main__":
    q = Queue()
    p = Process(target=Process_main, args=(q,))
    p.start()
    for i in range(20):
        q.put(random.randint(0,100000000))
    
    q.put(0)
    p.join()





