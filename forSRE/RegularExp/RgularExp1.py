import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d')
matches = pattern.finditer(text_to_search)


f = open("data.txt","r").read()
print f 

#matches = pattern.finditer(f)
matches = pattern.findall(f)


#matches = re.findall(r'\d\d\d.\d\d\d.\d\d\d',f)

for match in matches:
	print match