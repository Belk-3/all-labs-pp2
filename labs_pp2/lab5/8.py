import re 
x = input("Write here: ")
y = re.split("(?=[A-Z])",x)
print(y)
