"""
This Code will generate all the file and directories in a tree format 
This is an implimentation of tree command 
"""
import glob
import os

def tree(current_dir, level):
    level += 1
    all_current = glob.glob(current_dir)  # get all  current dir file

    for test in all_current:
        if "directory" in os.popen("stat "+test).read(500).split():
            if "/" in test:
                dirname = test.split("/")[-1]
            else:
                dirname = test

            indent = '  |' * (level-1) + '  +- '

            print "%s%s" % (indent, dirname)
            new_dir = test+"/*"
            tree(new_dir, level)

        elif "regular" in os.popen("stat "+test).read(500).split():
            if "/" in test:
                filename = test.split("/")[-1]
            else:
                filename = test
            indent = '  |' * (level) + '  +- '
            print "%s%s" % (indent, filename)
        else:
            if "/" in test:
                linkname = test.split("/")[-1]
            else:
                linkname = test
            linkto = os.popen("stat "+test).read(500).split()
            link = linkname+" --> " + linkto[3]
            indent = '  |' * (level) + '  +- '
            print "%s%s" % (indent, link)


level = 0
homedir = "*"
tree(homedir, level)
