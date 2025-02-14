#Генераторы (Generators) — это удобный способ создавать итераторы с помощью yield. 
#Они позволяют экономить память, так как не создают сразу весь список, а выдают
#элементы по мере запроса.

def my_gen():
    yield 2593
    yield 2
    yield 3
    yield 4

gen = my_gen()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3



# Lab work

def square_generator(N):
    for i in range(N + 1):
        yield i ** 2

# Тест
N = int(input("Введите число N: "))
for square in square_generator(N):
    print(square)
#====================================================================================
def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Введите число n: "))
for num in even_generator(n):
    if num == n and num % 2 == 0:
        print (num)
        break
    if num+1 == n and num % 2 == 0:
        print (num)
        break
    print(num, end=", ") 
#====================================================================================    
def div_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Введите n: "))
for num in div_by_3_and_4(n):
    print(num)
#==================================================================================== 
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a, b = map(int, input("Введите a и b: ").split())
for square in squares(a, b):
    print(square)
#====================================================================================
def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("Введите n: "))
for num in countdown(n):
    print(num)
