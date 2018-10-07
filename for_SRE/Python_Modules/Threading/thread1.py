#!/usr/bin/env python
import threading 

def run_this():
    global x 
    while x < 300:
        x +=1

    print x 

def do_after():
    global x 
    while x < 600:
        x +=1
    
    print x 


def main():
    global x 
    x = 0 

    our_thread = threading.Thread(target=run_this)
    our_thread.start()

    our_thread.join()

    our_thread1 = threading.Thread(target=do_after)
    our_thread1.start()
    our_thread1.join()



if __name__=="__main__":
    main()

