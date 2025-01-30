#Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#Note: If the item to remove does not exist, remove() will raise an error.

#Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#Note: If the item to remove does not exist, discard() will NOT raise an error.

#Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
