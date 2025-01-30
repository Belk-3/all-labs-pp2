# we have two main fucntion for sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

#Customize Sort Function we can do our sorting function
def myfunc(n):
  return abs(n - 50)



#=================================================================================

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# for it we create a new sort func. then use it with "key = ourFunction" in sort


# Case sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Luckily we can use built-in functions as key functions when sorting a list.
#So if you want a case-insensitive sort function, use str.lower as a key function:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# after it we get sorted by alphabet list
