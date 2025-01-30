# here we tolk about removing a items from list
thislist = [1,2,3,4,5,6,7,8,9,21381]
thislist.remove(21381)
print(thislist)
#If there are more than one item with the specified value, the remove() method removes the first occurrence:
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#['apple', 'cherry', 'banana', 'kiwi']

#removing by index
thislist = [1,4,5,6,7,8,7,9]
thislist.pop(1)
print(thislist)
#If you do not specify the index, the pop() method removes the last item.


#The del keyword also removes the specified index:
thislist = [1,4,5,6,7,8,7,9]
del thislist[3] #will remove a 6
#or if we dont write a index del will remove all list xDD


# also we can clear a index from all item 
thislist = [1,2,3,4,5,6]
thislist.clear()
print(thislist)