# to copy a list we have 1-2 methods

#Use the copy() method
#You can use the built-in List method copy() to copy a list.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Use the list() method
#Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

