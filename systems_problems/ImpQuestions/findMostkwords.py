def findMostkwords(filename):

    count_name = {}
    max_c = 0
    prev_c = 0
    mname = ""
    pname = ""

    with open(filename, "r") as read_pointer:
        for names in read_pointer:
            name = names.split()

            for n in name:
                if n not in count_name:
                    count_name[n] = 1
                else:
                    count_name[n] += 1

            """
            find a way to store in on one loop
            """


    print count_name, mname, pname

    for kname in sorted(count_name.items(), key=lambda x:x[1]):
        print kname[0], kname[1]

findMostkwords("text")
