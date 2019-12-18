from collections import Counter


def parseweblog(logfile):
    f = open(logfile,'r')
    hosts = {}
    for line in f:
        data = line.split()
        host = data[0]
        req = data[5]
        resCode = data[8]

        if host not in hosts:
            hosts[host] = [resCode]
        else:
            hosts[host] = hosts[host] + [resCode]

    return hosts


def main():
    result = {}
    logfile = "testLog.txt"
    respresult = parseweblog(logfile)
    for i,k in respresult.items():
        print i,k
        result[i] = Counter(k)


    output = sorted(result.items(), key=lambda x:x[1]['200'])
    print output





if __name__=="__main__":
    main()