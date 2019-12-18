import csv

"""
with open('name.csv', 'r') as re:
    line = csv.reader(re)

    with open('newname.csv','w') as wr:
        fline = csv.writer(wr)

        for name in line:
            fline.writerow(name)



with open('name.csv','r') as re:
    lines = csv.DictReader(re)

    with open('name1.csv','w') as wr:
        file_names = ['first_name','last_name','email']
        csv_writer = csv.DictWriter(wr, fieldnames=file_names, delimiter='\t')

        for line in lines:
            csv_writer.writerow(line)
"""


with open("test_copy.txt",'r') as re :
    for line in re:
        print line,
