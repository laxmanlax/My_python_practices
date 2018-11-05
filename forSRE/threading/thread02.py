#!/usr/bin/env python
import threading

def work():
    global x 
    while x< 300 :
        x +=1
        pass 
       
    print x

def do_after():
    global x 
    while x < 600:
        x +=1

    print x 

 
def main():
    global x 
    x = 0 
    my_thread = threading.Thread(target=work)
    my_thread.start()
    print my_thread.ident       ## Each thread has a thread identificatio no ..... if join() they are same without they are different 
    print threading.enumerate() ## This is see how many threads 
    my_thread.join()            ## let the first thread finish then start the second thread
    
    print threading.enumerate()

    next_thread = threading.Thread(target=do_after)
    next_thread.start()
    print threading.enumerate()

    print next_thread.ident
 

if __name__=="__main__":
    main()

