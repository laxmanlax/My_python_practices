#with open("text.txt", 'r') as f:
#    for line in f:
#        print line
#
#    # f_conts = f.read()
#    # print f_conts
#
#   # f_conts = f.readline()
#   # print f_conts
#
#    f_conts = f.readlines()
#    for i in f_conts:
#        print i
#

processdata ={}
f1 = open("text.txt",'r')
f_conts = f1.readlines()

for i in f_conts:
    success = 1
    clientError = 1
    serverError = 1
    hostcount = 1
    httpkey = i.split()[8]
    host = i.split()[0]

    if  host not in processdata.keys():
        if httpkey=="200":
            processdata[host] = [{httpkey:success}, hostcount]
        elif httpkey=="400":
            processdata[host] = [{httpkey:clientError}, hostcount]
        else:
            processdata[host] = [{httpkey: serverError}, hostcount]
    else:
        print  processdata

        if httpkey=="200":
            if httpkey not in processdata.values()[0][0]:
                processdata[host][0][httpkey]=success
                hostcount += processdata[host][1]
                processdata[host][1]=hostcount
            else:
                success += processdata[host][0][httpkey]
                hostcount += processdata[host][1]
                processdata[host][0][httpkey]=success
                processdata[host][1] = hostcount

        elif httpkey == "400":
            if httpkey not in processdata.values()[0][0]:
                processdata[host][0][httpkey] = clientError
                hostcount += processdata[host][1]
                processdata[host][1] = hostcount
            else:
                clientError += processdata[host][0][httpkey]
                hostcount += processdata[host][1]
                processdata[host][0][httpkey] = clientError
                processdata[host][1] = hostcount
        else:

            if httpkey not in processdata.values()[0][0]:
                processdata[host][0][httpkey] = serverError
                hostcount += processdata[host][1]
                processdata[host][1] = hostcount
            else:
                serverError += processdata[host][0][httpkey]
                hostcount += processdata[host][1]
                processdata[host][0][httpkey] = serverError
                processdata[host][1] = hostcount

print processdata
#print (f.name)
#f.close()
