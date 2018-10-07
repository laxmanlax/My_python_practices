from multiprocessing import Pool
import time 

def f(n):
    sum = 0
    for x in range(1000):
        sum +=x*x
    return sum 

def main():
    t1 = time.time()
    p = Pool()
    result = p.map(f, range(10000))
    p.close()
    p.join()

    print "Pool took :" ,time.time() - t1 
    t2 = time.time()
    result =[]

    for x in range(10000):
        result.append(f(x))
    
    print "Serial Process took :", time.time() - t2 

if __name__=="__main__":
    main()
    






