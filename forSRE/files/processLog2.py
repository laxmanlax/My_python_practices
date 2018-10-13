f = open("text2.txt","r")

result = {}
requestType = {}

for i in f:
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
        print result 
    else:
        TypeArr=[]
        CodeArr=[]
        
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
'''
# {"host":["rType":[{"status":[hostCount,rCount,resCount]}],rCount]}

    if host not in result:
        hostCount=1
        responceType[resCode] = [resCount, rTCount, hostCount]
        reqType[rType] = responceType
        result[host] = reqType
    else:

        print rType , result[host]
        if rType not in result[host]:
            rTCount = 1
            responceType[resCode] = [resCount, rTCount, hostCount]
            reqType[rType] = responceType
        else:
            if resCode not in responceType:
                resCount=1
                responceType[resCode] = [resCount, rTCount, hostCount]
            else:
                resCount = result[host][rType][resCode][0]+1

            rTCount=result[host][rType][resCode][1]+1

        hostCount = result[host][rType][resCode][2]+1
        result[host][rType][resCode]=[resCount, rTCount, hostCount]

print result
'''
