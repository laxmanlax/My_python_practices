import os

file_name = ""
maxsize = 0

for path, dirname, filename in os.walk("."):
    for fname in filename:

        mxfile = path + "/" + fname
        fsize = os.path.getsize(mxfile)

        if fsize > maxsize:
            maxsize = fsize
            file_name = fname



print file_name, maxsize
