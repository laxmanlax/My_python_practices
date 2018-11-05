#!/usr/bin/env python
import multiprocessing
# Sharing the data b/w two process

def calculte_Square(nums, result, v):
    v.value = 444
    for idx , val in enumerate(nums):
        result[idx]=val*val 

    print "Inside Process: {}".format(result[:])

def main():
    nums = [3,5,6,2,8,9]
    result = multiprocessing.Array('i',6) 
    v = multiprocessing.Value('i',0)
    
    p = multiprocessing.Process(target=calculte_Square, args=(nums, result, v))
    
    p.start()
    p.join()

    print result[:], v.value

if __name__=="__main__":
    main()