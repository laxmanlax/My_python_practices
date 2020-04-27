import time
import sys

def watch(fn, count=10):
    fp = open(fn, 'r')
    line_count = 1

    while True:
        new = fp.readline()

        if new and line_count <=  count:
            print new,
            line_count +=1
        else:
            time.sleep(0.5)


lins = sys.argv[1]
watch("text", int(lins))
