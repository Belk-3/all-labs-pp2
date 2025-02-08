# 4. Filter prime numbers from a list
import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    primes = list(filter(lambda x: is_prime(x), numbers))
    print(f"Prime numbers: {primes}")
    return primes
