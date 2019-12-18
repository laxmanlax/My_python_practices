import time

def watch(fn, line):
	fp = open(fn, 'r')

	count = 0 
	while True:
		new = fp.readline()

		if new:
			if count == line:
				break

			print new,
			count +=1
		else:
			time.sleep(0.5)


watch('test.txt', 10)