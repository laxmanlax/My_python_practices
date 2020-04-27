"""
Tree command Implimentations
"""
import glob
import os
import sys

def tree_cmd(path, level=0):
    level +=1
    all_files = glob.glob(path)

    for fname in all_files:

        if os.path.islink(fname):
            ftype = os.readlink(fname)
            indent = " |"*(level -1)+" +- "
            print "{}{} --> {}".format(indent,fname, ftype)
        else:
            ftype = fname

        if os.path.isdir(ftype):
            indent = " |"*(level -1)+" +- "
            print "{} {}".format(indent, level)
            tree_cmd(ftype+"/*", level)
        else:
            indent = " |"*(level -1)+" +- "
            print "{} {}".format(indent, level)

pathname = sys.argv[1]
tree_cmd(pathname)


def treeBFS(path):
    file_queue = glob.glob(path)

    while file_queue:
        fname = file_queue.pop(0)
        indent = len(fname.split("/")[:-2])

        if os.path.islink(fname):
            ftype = os.readlink(fname)
            print "{}{} --> {}".format(indent, fname, ftype)
        else:
            ftype = fname

        if os.path.isdir(ftype):
            print "{}{}".format(indent, ftype)
            sub_file = glob.glob(ftype+"/")
            file_queue = sub_file + file_queue
        else:
            print "{}{}".format(indent, ftype)


def parseLog(filename):
    count_resp = {}
    max_resp = 0
    pre_rspCount = 0
    mip = ""
    prevIp = ""

    with open(filename) as fp:
        for line in fp:
            data = line.split()
            ip = data[0]
            respcode = data[1]

            if ip not in count_resp and respcode == "200":
                count_resp[ip]  = 1
            else:
                count_resp[ip] += 1

            if ip  in count_resp and count_resp[ip] > max_resp:
                pre_rspCount = max_resp
                max_resp = count_resp[ip]
                mip = ip


            if max_resp > pre_rspCount and mip != ip:
                prevIp = ip


def readnReplce(filename):
    with open(filename, "r+") as readp:
        with open(filename, "r+") as writep:

            while True:

                nline = readp.newline()

                if not nline:
                    break
                update_line = nline.replace("old","new")
                writep.write(update_line)


def cmd_tail(filename, count):
    count_file = 1
    with open(filename, "r") as rp:

        while True:
            where = rp.tell()
            nline = rp.readline()

            if nline and count_file <= count:
                print line
            else:
                rp.seek(where)
                time.sleep()
