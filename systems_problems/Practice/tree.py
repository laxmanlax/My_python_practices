import glob
import os
import sys


def tree(cur_dir, level):
    level +=1
    all_cur_dirs = glob.glob(cur_dir)

    for fname in all_cur_dirs:
        if os.path.isdir(fname):
            if "/" in fname:
                dir_name = fname.split()[-1]
            else:
                dir_name = fname

            indent = "  |"*(level -1)+ " +- "
            print "{}{}".format(indent, dir_name)
            new_dir = fname+"/*"
            tree(new_dir , level)

        elif os.path.islink(fname):
            if "/" in fname:
                linkname = fname.split("/")[-1]
            else:
                linkname = fname

            indent = "  |"*(level -1)+ "  +- "
            linkto = os.popen("stat "+fname).read(500).split()
            link = linkname +"----->"+ linkto[3]
            print "{}{}".fromat(indent, link)
        else:
            if "/" in fname:
                filename = fname.split("/")[-1]
            else:
                filename = fname

            indent = "  |"*level+" +- "
            print "{}{}".format(indent, filename)

level = 0
currentdir = sys.argv[1]
tree(currentdir, level)
