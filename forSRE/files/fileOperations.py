# '''
# reading the complete file 
# ==================================
# '''
# 
f = open("sample.txt","r")
# 
#  for i in f:
#      print i.split()
#  
# 
# '''
# read()		#return one big string
# ==================================
# '''
# 
# #print f.read().split()
# 
# '''
# readline	#return one line at a time
# ==================================
# '''
# print f.readline()
# 
# 
# '''
# readlines	#returns a list of lines
# ===================================
# '''

Allclusters ={}
for items in f.readlines():
    cluster = items.split()[7]
    host = items.split()[0]
    if cluster not in Allclusters:
        Allclusters[cluster]=[host]
    else:
        Allclusters[cluster]=Allclusters[cluster]+[host]

print Allclusters 
download_dir="output.csv"
csv = open(download_dir,"w")

columnTitleRow = "CLUSTRT, HOSTS \n"
csv.write(columnTitleRow)

for clName, hosts in Allclusters.items():
    row = clName + " , " + " ".join(hosts) + "\n"
    csv.write(row)

'''
We can use Regex to search throught the file .... 
=================================================
'''

'''
import re 
print re.findall("\w+[1-9]-\w+[1-9]-[1-9]-\w+", f.read())
'''