import re 
x = input("Write here: ")
y = re.search("^ab*$",x)
if y:
    print(x)
else:
    print("No")
