#!/usr/bin/env python
import threading 

def run_this():
    x=0
    print "This is my Thread......."
    while not dead:
        x +=1 
        pass 
    print x 


def run_this1():
    x=0
    print "This is my Thread......."
    while not dead:
        x += 1
        pass
    print x


def run_this2():
    x=0
    print "This is my Thread......."
    while not dead:
        x += 1
        pass
    print x


def main():
    global dead
    x=0 
    dead = False 

    our_thread = threading.Thread(target=run_this)
    our_thread.start()
    our_thread = threading.Thread(target=run_this1)
    our_thread.start()
    our_thread = threading.Thread(target=run_this2)
    our_thread.start()



    print threading.active_count()
    print threading.enumerate()
    print threading.current_thread()

    raw_input("Hit enter to Die.......")
    dead = True 

if __name__ == "__main__":
    main()
