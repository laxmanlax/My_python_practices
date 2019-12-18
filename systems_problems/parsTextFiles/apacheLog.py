from collections import Counter

def parseweblog(logfile):
    f = open(logfile, "r")

    hosts = {}

    for i in f:
        data = i.split()
        host = data[0]
        req = data[5]
        resCode = data[8]

        if host not in hosts:
            hosts[host]= [resCode]
        else:
            hosts[host]= hosts[host]+[resCode]

    return hosts

def main():
    result = {}
    logfile="testLog.txt"
    respresult = parseweblog(logfile)

    #print respresult

    for i ,k in respresult.items():
        print i,Counter(k)
    #    item = {}

    #    for j in k:
    #        if j not in item:
    #            item[j] = 1
    #        else:
    #            item[j] = item[j] + 1

        result[i] =  Counter(k)

    output = sorted(result.items(), key=lambda x:x[1]['200'])
    print output

    #print result
if __name__=="__main__":
    main()
