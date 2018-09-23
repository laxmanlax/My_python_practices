#!/usr/bin/env python
import threading

def work():
    global x, lock 

    lock.acquire()
    try:
        while x< 300 :
            x +=1
            pass 
           
        print x
    finally:
        lock.release()

def do_after():
    global x, lock 

    lock.acquire()
    try:
        while x< 600 :
            x +=1
            pass 
           
        print x
    finally:
        lock.release()
 
def main():
    global x , lock
    x = 0 
    lock = threading.Lock()  ## Locks memory so that other process will not use it 

    my_thread = threading.Thread(target=work)
    my_thread.start()
    

    next_thread = threading.Thread(target=do_after)
    next_thread.start()

 

if __name__=="__main__":
    main()

