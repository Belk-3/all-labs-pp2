import re 
x = input("Write here: ")
y = re.findall(r"\b[A-Z]{1}+[a-z]+\b" , x)
if y:
    print(y)
else:
    print("No")
