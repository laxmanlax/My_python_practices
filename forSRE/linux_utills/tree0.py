import os 
import glob 
import sys
pathname = sys.argv[1]

def is_tree(current_dir,level):
    level +=1
    all_files = glob.glob(current_dir)

    for fname in all_files:
        if os.path.isdir(fname):
            if "/" in fname:
                dirname = fname.split("/")[-1]
            else:
                dirname = fname
            indent = "  |"*(level-1)+" +- "
            print "{}{}".format(indent, dirname)
            new_dir=fname+"/*"
            is_tree(new_dir,level)

        elif os.path.islink(fname):
            if "/" in fname:
                linkname = fname.split("/")[-1]
            else:
                linkname = fname
            indent = "  |"*level+" +- "
            linkto = os.popen("stat "+fname).read(500).split()
            link=linkname +"-----> "+ linkto[3]
            print "{}{}".format(indent, link)
        else:
            if "/" in fname:
                filename = fname.split("/")[-1]
            else:
                filename = fname 
            indent = "  |"*level+" +- "
            print "{}{}".format(indent, filename)

level = 0 
current_dir=pathname
is_tree(current_dir,level)
