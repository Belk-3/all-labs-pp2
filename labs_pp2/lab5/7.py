import re 
x = input("Write here: ")
y = re.sub(r"_([a-z])", lambda match: match.group(1).upper(),x)
print(y)
