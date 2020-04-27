#Find all files with ending with .py using glob
import glob
import fnmatch
import os

"""
Finding all the files ending with .py in the current directory
"""
dirlist = glob.glob("/home/vagrant/*")
for dir in dirlist:
    if fnmatch.fnmatch(dir,"*.py"):
        print os.path.basename(dir)


"""
Find all the files ending with .py in the entire directory tree
"""
def find_all(working_dir):
    fnd_names = glob.glob(working_dir)

    for name in fnd_names:
        if os.path.isdir(name):
            find_all(name)
        else:
            if name.split(".")[-1] == "py":
                print name

find_all("/home/vagrant/*")

"""
Find all the files and dirctories have the name <----> in the entire directory tree
"""
def find_all(path):
    fndnames = glob.glob(path)

    for fnd in fndnames:
        if os.path.isdir(fnd):
            fname = fnd.split("/")[-1]
            if fnmatch.fnmatch(fname,"*fork*"):
                print fnd
            f  = fnd +"/*"
            find_all(f)
        else:
            fname = fnd.split("/")[-1]
            if fnmatch.fnmatch(fname,"*fork*"):
                print fnd

find_all("/home/vagrant/*")
