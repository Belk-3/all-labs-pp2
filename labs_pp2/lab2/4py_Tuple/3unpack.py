#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

# we use when wanna get a another value than in tuple for it 
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
