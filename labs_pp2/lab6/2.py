n = str(input("Че за пароль ?"))
g = 0
l = 0
for i in n:
    if ord(i) >= 65 and ord(i) <= 90:
        g += 1
    elif ord(i) >= 97 and ord(i) <= 122:
        l += 1
print(l , " ", g)