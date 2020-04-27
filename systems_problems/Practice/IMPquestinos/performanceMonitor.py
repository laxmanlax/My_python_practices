import platform
import subprocess
import time

"""
Write Using linux internal tools
"""

def cpuInfo():
	with open("/proc/cpuinfo") as f:
		for line in f:
			print line.strip("\n")


def memInfo():
	with open("/proc/meminfo") as f:
		for line in f:
			print line


def networkStat():
	with open("/proc/net/dev") as f:
		for line in f:
			print lines


def allpids():
	with open("/proc/[1-9]*/stat") as f:
		for line in f:
			print line


def size(device):
	nr_sectors = open(device+"/size").read().rstrip("\n")
	sect_size = open(device+'/queue/hw_sector_size').read().rstrip('\n')
	return (float(nr_sectors)*float(sect_size))/(1024.0*1024.0*1024.0)



def blockDevices():
	for device in glob.glob("/sys/block/*"):
		if re.compile("sd*").match(os.path.basename(device)):
			print "Device:: {0}, Size:: {1} GiB".format(device, size(device))


def DiskStat():
	df = subprocess.Popen([“df”,”-h”], stdout=subprocess.PIPE)
	for line in df.stdout:
		splitline = line.decode().split()
		if splitline[5] == partition:
			if int(splitline[4][:-1]) > threshold:
				print "__"



def linux_monitor():

	while True:
		print cpuinfo()
		print meminfo()
		print networkStat()
		print allpids()
		print blockDevices()
		print DiskStat()

		time.spleep(10)



if __name__=="__main__":
	linux_monitor()









	


