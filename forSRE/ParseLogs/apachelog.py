"""
This function process big web apache log file with all it's  responce details 
Sample Data-Structure  
----------------------
{"host":[{"rType":[{"status":rSCount}, rTCount]},HCount]

"""
def parseweblog(logfile):
    f = open(logfile, "r")
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
    
    return result 

def main():
    logfile="text.txt"
    print parseweblog(logfile)

if __name__=="__main__":
    main()