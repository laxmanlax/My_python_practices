import glob
import os
import sys

userDir = sys.argv[1]

def tree(currDir, level):
    level +=1
    current_dir = glob.glob(userDir)

    for fname in current_dir:
        if os.path.isdir(fname):
            if "/" in fname.split("/"):
                dirname = fname.split("/")[-1]
            else:
                dirname = fname
            indent = "   |"*level-1+" +- "
            print "{} {}".format(indent, dirname)
            newDir = dirname + "/*"
            tree(newDir,level)

        elif os.path.link(fname):
            if "/" in fname.split("/"):
                linkName = fname.split("/")[-1]
            else:
                linkName = fname
            indent = "  |"*level+" +- "
            linkto = os.popen("stat ", fname).readlines(200)[3]
            link = linkName ,"--->>", linkto
            print "{}{}".format(indent, link)
        else:
            if "/" in fname.split("/"):
                fileName = fname.split("/")[-1]
            else:
                fileName = fname
            indent = "  |"*level+" +- "
            print "{}{}".format(indent, fileName)

level = 0
currDir = userDir
tree(currDir, level)
