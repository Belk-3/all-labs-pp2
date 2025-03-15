n = str(input("Name ?: "))
a = int(len(n)/2)
for i in range(a):
    if n[i] != n[-(i+1)]:
        print("NO polidrom")
        exit()
print("Polindrom")
        

    
        

