import re

str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
print match
if match:
  print 'found', match.group() ## 'found word:cat'
else:
  print 'did not find'


## Search for pattern 'iii' in string 'piiig'.
## All of the pattern must match, but it may appear anywhere.
## On success, match.group() is matched text.
match = re.search(r'iii', 'piiig') # found, match.group() == "iii"

if match:
  print 'found', match.group() ## 'found word:cat'
else:
  print 'did not find'

match = re.search(r'igs', 'piiig') # not found, match == None

if match:
  print 'found', match.group() ## 'found word:cat'
else:
  print 'did not find'

## . = any char but \n
match = re.search(r'..g', 'piiig') # found, match.group() == "iig"
if match:
  print 'found', match.group() ## 'found word:cat'
else:
  print 'did not find'

## \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'p123g') # found, match.group() == "123"
if match:
  print 'found', match.group() ## 'found word:cat'
else:
  print 'did not find'

match = re.search(r'\w\w\w', '@@abcd!!') # found, match.group() == "abc"
if match:
  print 'found', match.group() ## 'found word:cat'
else:
  print 'did not find'

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'[a-z-]+@\w+', str)
if match:
    print match.group()

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'([\w.-]+)@([\w.-]+)', str)

if match:
  print match.group()   ## 'alice-b@google.com' (the whole match)
  print match.group(1)  ## 'alice-b' (the username, group 1)
  print match.group(2)  ## 'google.com' (the host, group 2)


str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str)
print emails

for email in emails:
    print email



f = open('testLog.txt', 'r')
strings = re.findall(r'\d+\.\d+\.\d+\.\d+', f.read())
match = re.search(r'\d+\.\d+\.\d+\.\d+', f.read())
print strings


if match:
  print(match.group())
else:
  print("pattern not found")
