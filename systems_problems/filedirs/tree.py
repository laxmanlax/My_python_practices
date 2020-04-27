import glob
import os


def tree(path, level=0):
    level +=1

    dirnames = glob.glob(path)
    for fname in dirname:
        if os.path.isdir(fname):
            indent = "  |"*(level -1)+" +- "
            print "{}{}".format(indent, fname)

            newdir = fname + "/*"
            tree(newdir, level)
        else:
            indent = "  |"*(level -1)+ " +- "
            print "{}{}".format(indent, fname)



level = 0


tree()
