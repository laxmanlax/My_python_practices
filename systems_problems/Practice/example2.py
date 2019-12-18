import csv


with open('test.csv','r') as rline:
    read_file = csv.reader(rline)
    with open("result.csv","w") as wline:
        write_line = csv.writer(wline, delimiter="\t")

        for line in read_file:
            print line
            write_line.writerow(line)




print "="*50 ,"\n"



with open('test.csv','r') as read_l:
    read_line = csv.DictReader(read_l)

    with open('result1.csv', 'w') as write_l:
        file_names = ['first_name','last_name','email']

        write_line = csv.DictWriter(write_l, filenames=file_names, delimiter="\t")

        for line in read_line:
            write_line.writerow(line)
