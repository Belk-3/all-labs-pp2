import re 
x = input("Write here: ")
y = re.fullmatch("^a.*b",x)

if y:
    print("Yes")
else:
    print("No")
