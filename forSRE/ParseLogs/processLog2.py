f = open("text.txt","r")

result = {}

for i in f:
    requestType = {}
    requestCode = {}


    HCount = 1
    rTCount = 1
    rSCount = 1

    host = i.split()[0]
    reqType = i.split()[5].replace('"',"")
    reqCode = i.split()[8]

    '''
    #print host, reqType, reqCode
    {"host":[{"rType":[{"status":rSCount}, rTCount]},HCount]
    '''

    if host not in result:
        requestCode[reqCode]=rSCount
        requestType[reqType] = [requestCode, rTCount]
        result[host] = [requestType, HCount]
    else:
        result[host][1]+=1

        if reqType in result[host][0]:

            if reqCode in result[host][0][reqType][0]:
                result[host][0][reqType][0][reqCode] +=1
            else:
                requestCode = result[host][0][reqType][0]
                requestCode[reqCode]=rSCount

            result[host][0][reqType][1]+=1
        else:
            requestCode[reqCode]=rSCount
            requestType = result[host][0]
            requestType[reqType]=[requestCode,rTCount]

print result 