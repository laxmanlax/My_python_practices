import re
from collections import Counter

def parsefile(filename):
    with open(filename, 'r')  as f:
        count = {}
        for i in f:
            host = i.split()[0]
            if host not in count:
                count[host] = 1
            else:
                count[host] = count[host]+1

    return count

def example1(filename):
    host_list = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" , open(filename, 'r').read())
    #return Counter(host_list)

    for host in host_list:
        count[host] = 1
    else:
        count[host] = count[count] + 1
    return count


def example2(filename):
    host_list = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", open(filename, 'r').read())
    return Counter(host_list)


def main():
    print parsefile('test.txt'),"\n"
    print parsefile('test.txt'),"\n"
    print example2('test.txt')


if __name__=='__main__':
    main()
