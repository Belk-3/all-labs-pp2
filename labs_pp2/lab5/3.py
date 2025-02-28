import re 
x = input("Write here: ")
y = re.findall(r"\b[a-z]+_[a-z]+\b",x)

if y:
    print(x)
else:
    print("No")
