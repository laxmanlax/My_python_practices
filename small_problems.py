input = [
          ('11013331', 'KAT'),
          ('9085267',  'NOT'),
          ('5238761',  'ETH'),
          ('5349618',  'ETH'),
          ('11788544', 'NOT'),
          ('962142',   'ETH'),
          ('7795297',  'ETH'),
          ('7341464',  'ETH'),
          ('9843236',  'KAT'),
          ('5594916',  'ETH'),
          ('1550003',  'ETH')
        ]
t1={}
def group_by(input):
    for i,j in [(i[1], i[0]) for i in input]:
        if i not in t1.keys():
            t1.update({i:[j]})
        else:
            print "ok" ,t1[i]
            t1.update({i: t1[i]+ [j]})
    return t1

print group_by(input)

######################################################

def pairSum1(arr, k):
    if len(arr)<2:
        return
    arr.sort()
    left, right = (0, len(arr)-1)
    while left<right:
        currentSum=arr[left]+arr[right]
        if currentSum==k:
            print arr[left], arr[right]
            left+=1 #or right-=1
        elif currentSum<k:
            left+=1
        else:
            right-=1

arr = [5, 6, 4, 7, 3, 4, 5, 6, 3, 1, 2, 4]
k = 6
pairSum1(arr, k)


arr = [5, 6, 4, 7, 3, 4, 5, 6, 3, 1, 2, 4]
k = 6

def pairSum2(iterable,m):
 increment=0
 for i in range(len(iterable)):
     increment +=1
     for j in range(len(iterable))[increment:]:
         if (arr[i]+arr[j])==k:
             print arr[i],arr[j]

pairSum2(arr,k)

##################################################

def compress(string):
    prev = None
    cons = 1
    compress = ''
    for i in string:
        if prev:
            if prev  == i:
                cons += 1
            else:
                compress += prev+str(cons)
                cons = 1
        prev = i
    compress += prev+str(cons)
    return compress
print compress("aaaaabababbbaaaaa")

###################################################
def balance_braces(braces):
    brace_all = {
             '(':')',
             '[':']',
             '{':'}'
             }
    sub_br = brace_all.values()
    list_1=[]
    for i in braces:
        if i in brace_all.keys():
            list_1.append(i)
        elif i in sub_br and (brace_all[list_1[-1]] == i):
            list_1.pop()
    return list_1 ==

print balance_braces("{{()[]}}{")

#####################################################
#######-----------iterables----------------#########

def accumulate(iterable):
    int_list=[]
    value=1
    for i in iterable:
        next_val=value*i
        value=next_val
        print value

accumulate([1,2,3,4,5])


def chain(*iterable):
    print iterable
    for i in iterable:
        for j in i:
            print j,

chain('abc','def')


def combination(iterable, r):
    keep=''
    list1=[]
    for i in list(iterable):
        keep=i
        for j in list(iterable):
            if keep == j:
                pass
            list1.append(i+j)
    return list1


def combination(iterable):
    increment=0
    for i in range(len(iterable)):
        increment +=1
        for j in range(len(iterable))[increment:]:
            print iterable[i]+ iterable[j]

            #if iterable[i] == iterable[j]:
            #    pass
            #else:
            #    print iterable[i]+ iterable[j]

combination('ABCD')


def combination(iterable):
    for i in range(len(iterable)):
        for j in range(len(iterable)):
            j+=1
            print iterable[i:j]

combination('ABCD')


def perm(a,k=0):
   if(k==len(a)):
      print a
   else:
      for i in xrange(k,len(a)):
         a[k],a[i] = a[i],a[k]
         perm(a,k+1)

print permutations([2,4,3])

def combination(iterable):
 increment=0
 for i in range(len(iterable)):
     increment +=1
     for j in range(len(iterable))[increment:]:
         print iterable[i] , iterable[j]


combination([1,2,3,4,6])

####################################################
#Question:
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

def find_dev():
    l=[]
    for i in range(3200-2000):
        if i%7==0 and i%5!=0:
            l.append(str(i))
    print ','.join(l)

find_dev()

#################################################
#####---------factorial-------------------#######

##3*2*1
def fac(n):
    num=1
    if n!=0:
        for i in range(1,n+1):
            num=num*i
        return num
    return 0
print fac(4)

def factorial(n):
    base = 1
    for i in range(n,0,-1):
        base = base * i
     print base

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print fact(8)

###################################################
###---------------files----------------------####

print open('foo.txt').read()

print open('foo.txt').readlines()

def charcount(l):
    return len(open('foo.txt').read())
print charcount('foo.txt')

def wordcount(l):
    return len(open('foo.txt').read().split())
print wordcount('foo.txt')

def linecount(filename):
    return open(filename).readlines()
print linecount('foo.txt')

#print each line of a file in reverse order.

def linecount(filename):
    t1=[]
    tt = open(filename).readlines()
    for i in tt:
        t1.append(" " .join(i.split()[::-1]))

    return t1
print linecount('foo.txt')

##################################################
##### count the no of occurence   ######

def find_substring(string, sub_str):
    count =0
    for i in range(len(string)):
        if string[i:i+len(sub_str)]== sub_str:
            count+=1
    return count

print find_substring("CDCACDCBCDCDCCDC","CDC")



################################################
###---------- sublist ----------------######
def sublist(ll)
    t2=[]
    for i in ll:
        t1=[]
        for j in ll:
            if ''.join(sorted(i))==''.join(sorted(j)) and len(i) == len(j):
                t1.append(j)
        if t1 in t2:
            pass
        else:
            t2.append(t1)
    return t2

print sublist(ll)

################################################
#######----anagram---------#########
def anagram(l):
    tt = map(lambda x:''.join(sorted(x)),l)
    t1 =[]
    t2=[]
    for i in l:
        if ''.join(sorted(i)) in tt:
            t1.append(i)
        else:
            pass

        t2.append(t1)

    return t2

l = ['eat', 'ate', 'done', 'tea', 'soup', 'node']

print anagram(l)

###########################################
