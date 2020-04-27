from collections import Counter

with open('testLog.txt', 'r') as r:
    hosts = {}
    for i in r:
        logs = i.split()
        ip = logs[0]
        req = logs[5]
        resp = logs[8]

        #print ip ,"  ",req,"  ",resp

        if ip not in hosts:
            hosts[ip] = [resp]
        else:
            hosts[ip] += [resp]

    result = {}
    
    for k,v in hosts.items():
        result[k]=Counter(v)


    print sorted(result.items(), key=lambda x:x[1]['200'])







