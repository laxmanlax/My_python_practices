import re

text = "John Doe \n Jane Doe \n Jin Du \n Chin Doe"
results = re.split(r"\n+", text)
print results     # will print: ['Jane Doe', 'Jane Doe', 'Jin Du', 'Chin Doe']
print "***************************************************************************** \n"


pattern = re.compile(r"[0-9]+")
result = pattern.sub("__", "there is only 1 thing 2 do")
print result 
print "***************************************************************************** \n"


pattern = re.compile(r"\w+") # Match only alphanumeric characters
input_string = "Lorem ipsum with steroids"
result = pattern.sub("regex", input_string) # replace with the word regex
print result  # prints 'regex regex regex regex'
print "***************************************************************************** \n"


"""
Match any word followed by a comma.
The example below is not the same as re.compile(r"\w+,")
For this will result in [ 'me,' , 'myself,' ]
"""
pattern = re.compile(r"\w+(?=,)")
res = pattern.findall("Me, myself, and I")
print res
print "***************************************************************************** \n"


