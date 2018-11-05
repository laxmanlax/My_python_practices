#!/usr/bin/env python 
import Queue
import threading
import urllib2 

def get_url(q, url):
    q.put(urllib2.urlopen(url).read())

def main():
    theurls = ["http://google.com", "http://yahoo.com"]
    q = Queue.Queue()
    for u in theurls:
        t1 = threading.Thread(target=get_url, args=(q, u))
        t1.start()
    
    while q.empty():
        print q.get()


if __name__=="__main__":
    main()

