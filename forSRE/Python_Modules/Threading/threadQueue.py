#producer and consumer threads communicating with a shared queue
# https://www.agiliq.com/blog/2013/10/producer-consumer-problem-in-python/   

import threading
import Queue
import time

numconsumer = 2
numproducer = 4
nummessages = 4

dataQueue = Queue.Queue()


def producer(idnum, dataqueue):
    for msgnum in range(nummessages):
        time.sleep(idnum)
        dataqueue.put('[producer id=%d, count=%d]' % (idnum, msgnum))

def consumer(idnum, dataqueue):
    while True:
        time.sleep(0.2)
        try:
            data = dataQueue.get(block=False)
        except Queue.Empty:
            pass 
        else:
            print "consumer :", idnum, "got =>", data

def main():
    for num in range(numconsumer):
        thread = threading.Thread(target=consumer, args=(num,dataQueue))
        thread.daemon = True
        thread.start()

    waitfor=[]
    for i in range(numproducer):
        thread = threading.Thread(target=producer, args=(i,dataQueue))
        waitfor.append(thread)
        thread.start()

    for thread in waitfor:
        thread.join()

    print "Main Thread exits.........."

if __name__=="__main__":
    main()
