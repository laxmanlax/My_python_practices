testVal = [1,7,5,3,8,2]

for i in range(len(testVal)-2):
    imin = i
    for j in range(1,len(testVal)-1):
        if testVal[imin] > testVal[j]:
            imin = j

    temp = testVal[i]
    testVal[i] = testVal[imin]
    testVal[imin] = temp 

print testVal









i-dev1-master-r407.c.gsf-core-devmvp-hbase.internal



:%s/localhost/i-dev1-master-r407.c.gsf-core-devmvp-hbase.internal/g





