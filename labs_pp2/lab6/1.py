a = []
n = int(input("сколько значений добавить ? : "))
for i in range(n):
    a.append(int(input()))

for i in range(n):
    a[i] = pow(a[i],2)

print(a)