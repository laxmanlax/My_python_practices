import csv

with open('test.csv', 'r') as csvFile:
    r = csv.reader(csvFile)
    for i in r:
        print i

#f = open('test.txt','r')
with open('test.txt', 'r') as f:
    #f_read = f.read()
    #print (f_read)

    #f_read = f.readline()
    #print (f_read)

    for line in f:
        print (line)


with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


with open('test.txt', 'r') as rf:
    with open('test_copy1.txt', 'w') as wf:
        chunk_size = 20
        chunk = rf.read(chunk_size)
        while len(chunk) > 0:
            wf.write(chunk)
            chunk = rf.read(chunk_size)
