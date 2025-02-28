import re 
x = input("Write here: ")
y = re.sub("([a-z])([A-Z])" , r"\1_\2",x).lower()
print (y)
