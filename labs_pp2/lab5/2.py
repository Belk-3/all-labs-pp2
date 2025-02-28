import re 
x = input("Write here: ")
y = re.fullmatch("^ab{2,3}",x)

if y:
    print(x)
else:
    print("No")



