import re 

pattern = re.compile(r"\w+\s\w+\s\w+")
string = "regex is amazing"
result = pattern.match(string)
print result.group()
