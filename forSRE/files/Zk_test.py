import os
from subprocess import Popen, PIPE
import sys
import datetime

tt = "echo get /my_sample_zode | zookeeper-shell atl1q00kzkp01.qa.local:2181,atl1q00kzkp02.qa.local:2181,atl1q00kzkp03.qa.local:2181"
f = os.popen(tt).readlines()

for line in f:
    print line.split()
    if line.split() != [] and line.split()[0] == "sample_data_1":
        print "---------- {}".format(line)
