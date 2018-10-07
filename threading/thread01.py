#!/usr/bin/env python
import threading
def work():
    print "This is first thread.........."
    x = 0
    while not dead:
        x +=1
        pass

    print x


def main():
    global dead
    dead = False

    my_thread = threading.Thread(target=work)
    my_thread.start()

    print threading.active_count()
    print threading.enumerate()
    print threading.current_thread()
    print my_thread.is_alive()
    
    raw_input("Hit enter to stop......")
    dead = True
    raw_input("The is alive wait for bit ......")
    print my_thread.is_alive()

if __name__=="__main__":
    main()
