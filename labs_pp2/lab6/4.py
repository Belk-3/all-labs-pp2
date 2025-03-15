import time
import math

n = int(input("root of this ? : "))
sleep = int(input("milliseconds: " ))
time.sleep(sleep/1000)

print(f"square root of {n} after {sleep} miliseconds is ",math.sqrt(n))