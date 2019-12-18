#Print all process status
import glob
import  fnmatch
import os

dirlist = glob.glob('/home/vagrant/*')
#print dirlist

for dir in dirlist:
    if fnmatch.fnmatch(dir,"*.py"):
        print os.path.basename(dir)

flist = glob.glob('/proc/[0-9]*/stat')

#print flist
#tab=" "
#for files in flist:
#    print tab,list(open(files))[0].split()[0],"----",list(open(files))[0].split()[1]
#    tab+=" "

for file in glob.glob('/proc/[0-9]*/stat'):
    print list(open(file))[0].split()[0] ," -->> " , list(open(file))[0].split()[1]


for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.py'):
        print file


dirlist = glob.glob('/proc/[0-9]*/stat')

tab=" "
for dir in dirlist:
    process=os.popen("cat "+dir+"").readline()
    print " |",process.split()[0],process.split()[1]
    if process.split()[2]=="S":
        print " |","+ --","SLEEPING"

    tab+="-"


import json
d = {'alpha': 1, 'beta': 2}
s = json.dumps(d)
open("out.json","w").write(s)
