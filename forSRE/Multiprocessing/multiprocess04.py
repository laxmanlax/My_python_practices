#!/usr/bin/env python
import multiprocessing
# Sharing the data b/w two process using Queue 

def calculte_Square(nums,q):
    for n in nums:
        q.put(n*n)


def main():
    nums = [3,5,6,2,8,9]
    q = multiprocessing.Queue() # Lives in shared memory Used to share data b/w process  
    p = multiprocessing.Process(target=calculte_Square, args=(nums, q))
    
    p.start()
    p.join()

    while not q.empty():
        print q.get()



if __name__=="__main__":
    main()