processData = {}

fdata = open("text.txt")
f = fdata.readlines()

'''
DataStructure  Design 
=====================
Ex : = Data Structure 
{"host": [{"GET": [{"200": statuscount, "500": statuscount, "400": statuscount}, reqestCount], "POST": [{"200": statuscount, "500": statuscount, "400": statuscount}, reqestCount], 
"DELETE": [{"200": statuscount, "500": statuscount, "400": statuscount}, reqestCount]}, hostcount]}
'''

def ProcessApachelog(f):
    allStatus = {}
    allRequests = {}

    for line in f:
        hostcount = 1
        reqestCount = 1
        statuscount = 1
    
        host= line.split()[0]
        rType = line.split()[5].replace('"',"")
        status = line.split()[8]
    
        if str(host) not in processData.keys():
            rCount = [reqestCount]
            reqType = [hostcount]
            allStatus[status]=statuscount
    
            rCount.append(allStatus)
            allRequests[rType] = rCount
            reqType.append(allRequests)
            processData[host] = reqType
        else:
            allRequests = processData[host][1]
            hostcount +=processData[host][0]
            reqType = processData[host]
            reqType[0]=hostcount
    
            if rType not in processData[host][1]:
                rCount = [reqestCount]
                allStatus[status] = statuscount
                rCount.append(allStatus)
                allRequests[rType] = rCount
                processData[host] = reqType
                
            else:
                allStatus = processData[host][1][rType][1]
                rCount = processData[host][1][rType]
                reqestCount += processData[host][1][rType][0]
                rCount[0] = reqestCount
                if status not in processData[host][1][rType][1]:
                    allStatus[status] = statuscount
                else:
                    statuscount += processData[host][1][rType][1][status]
                    allStatus[status] = statuscount
                allRequests[rType] = rCount
                processData[host] = reqType
        
    print processData,("\n")*3 

def main():
    try:
        ProcessApachelog(f)
    except Exception as e:
        pass 



if __name__=="__main__":
    main()