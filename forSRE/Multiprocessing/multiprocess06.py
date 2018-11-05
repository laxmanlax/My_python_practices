#!/usr/bin/env python 
from multiprocessing import Pool as ThreadPool 
import urllib2 

urls = [
  'http://www.python.org', 
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
]
# make the pool of workers 
pool = ThreadPool(5)
result = pool.map(urllib2.urlopen, urls)

pool.close()
pool.join()



