import sys


def tail(line_count=0, filename="test.txt"):
	if line_count > 0:
		with open(filename,'r') as read:
			count = 0
			for line in read:
				if count == int(line_count):
					break
				else:
					print line, 
				count +=1
	else:
		with open(filename,'r') as read:
			for line in read:
				print line,


file = sys.argv[0:]
file_name = file[1]
count = 0
if len(file) > 2:
	count = int(file[2])

tail(int(count), file_name)

