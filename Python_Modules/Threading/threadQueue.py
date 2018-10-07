#producer and consumer threads communicating with a shared queue
#https://www.agiliq.com/blog/2013/10/producer-consumer-problem-in-python/
import threading
import Queue
import time

numconsumer = 2
numproducer = 4
nummessages = 10

dataQueue = Queue.Queue()

def producer(idnum, dataqueue):
    for msgnum in range(nummessages):
        time.sleep(0.2)
        dataqueue.put('[producer id : {}, count  :  {}]'.format(idnum, msgnum))

def consumer(idnum, dataqueue):
    while True:
        time.sleep(0.2)
        try:
            data = dataQueue.get()
        except Queue.Empty:
            pass
        else:
            print "Consumer ---->>  {} got ----->>  {}".format(idnum, data)

def main():
    for num in range(numconsumer):
        thread = threading.Thread(target=consumer, args=(num,dataQueue))
        thread.deamon = True
        thread.start()

    waitfor=[]

    for num in range(numproducer):
        thread = threading.Thread(target=producer, args=(num,dataQueue))
        waitfor.append(thread)
        thread.start()

    for thread in waitfor:
        thread.join()

    print "Main Thread exits.........."

if __name__=="__main__":
    main()
