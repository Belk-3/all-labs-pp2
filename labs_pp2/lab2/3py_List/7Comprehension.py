#i dont know how it write but i will just write 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# we can rewrite like 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# i dont know how it works xDDD
# newlist = [expression for item in iterable if condition == True]
# here we can see a formula of this 
# expression its a item which we want to add
# for x in fruits is a loop
# next one is condition when a x item will in newlist

#The iterable can be any iterable object, like a list, tuple, set etc.
# we can use alsa a range 

newlist = [x for x in range(10)]

#here with condition
newlist = [x for x in range(10) if x < 5]