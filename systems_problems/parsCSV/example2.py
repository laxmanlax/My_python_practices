import csv

"""
with open('name.csv', 'r') as csv_name:
    csv_read = csv.reader(csv_name)

    #next(csv_name)
    with open('new_name.csv', 'w') as new_file:
        csv_write = csv.writer(new_file, delimiter='\t')

        for names in csv_read:
            line = [names[0],names[2]]
            csv_write.writerow(line)


with open('name.csv', 'r') as csv_name:
    csv_read = csv.DictReader(csv_name)
    #for line in csv_read:
    #    print line
    with open('new_name.csv', 'w') as new_write:
        file_names = ['first_name','last_name','email']

        csv_writer = csv.DictWriter(new_write, fieldnames=file_names, delimiter='\t')

        for line in csv_read:
            csv_writer.writerow(line)

"""
import re

temp = open('name.csv', 'r').read()
emails = re.findall(r'[\w\.-]+@[\w\.-]+', temp)

for email in emails:
    print email

# Open file
f = open('test.txt', 'r')
# Feed the file text into findall(); it returns a list of all the found strings
strings = re.findall(r'some pattern', f.read())


str = "The rain in Spain"
x = re.split("\s", str)
print(x)
