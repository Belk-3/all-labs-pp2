thislist = [1,2,3,4,5,6,7,8,9]
thislist.append(0)
print(thislist)
# appens just add a new item at the end of list


# to add a items from another list to current we use extend()
h = [9,8,7,6,5,4,3,2,1]
thislist.extend(h)
print(thislist)

# when we use a extend() it doesnt matter what type of list is for ex. : we can add list and turple
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)



