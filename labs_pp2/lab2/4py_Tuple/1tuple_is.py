""""
Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets

"""

thistuple = ("apple", "banana", "cherry")
print(thistuple)

""""
When we say that tuples are ordered, it means that the items have a defined order, 
and that order will not change.


Tuples are unchangeable, meaning that we cannot change, add or remove items 
after the tuple has been created.

Allow Duplicates
"""

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Create Tuple With One Item
#To create a tuple with only one item, you have to add a
# comma after the item, otherwise Python will not recognize it as a tuple.


thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))



#The tuple() Constructor
#It is also possible to use the tuple() constructor to make a tuple.


thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
f = [1,4]
