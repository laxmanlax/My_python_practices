import os
import sys
import fnmatch

for dirpath, dirname, filename in os.walk("."):
    print "Current Path:===>> ", dirpath
    print "Directories:====>>",  dirname
    print "Files:==========>>",  filename
    print ("  ")



for path, dirname, filename in os.walk("."):
    print "[ --------" + path + "----------]"
    for fname in filename:
        print os.path.join(path, fname)


dirname = sys.argv[1]
allfile=[]
for path_ , dir_name, filename in os.walk(dirname):
    print filename
    for j in filename:
        print "------",j,os.stat(j).st_size


#Find files all files ending with .py
for dirpath, dirs, files in os.walk("."):
    for filename in fnmatch.filter(files, "*.py"):
        print filename


#Find largest file
maxsize = 0
file_name = ""
pathname = sys.argv[1]
for filename in os.listdir(pathname):
    path = pathname +"/"+filename
    if not  os.path.isdir(path):
        if maxsize < os.path.getsize(path):
            maxsize = os.path.getsize(path)
            file_name = path


print file_name
maxsize = 0
file_name = ''
pathname = sys.argv[1]
for path, dirname , filename in os.walk(pathname):
    file_path = os.path.join(path, filename)

    if os.path.isfile(file_path):
        if maxsize < os.path.getsize(path):
            maxsize = os.path.getsize(path)
            file_name = path
