#Sets are used to store multiple items in a single variable.
#A set is a collection which is unordered, unchangeable*, and unindexed.
# Note: Set items are unchangeable, but you can remove items and add new items.
#==========================================================================================================
#to create set:
thisset = {"apple", "banana", "cherry"}
print(thisset)
#==========================================================================================================
#Note: Sets are unordered, so you cannot be sure in which order the items will appear.
#Set items are unordered, unchangeable, and do not allow duplicate values.
#==========================================================================================================
#Unordered means that the items in a set do not have a defined order.
#==========================================================================================================
#Set items can appear in a different order every time you use them, 
#and cannot be referred to by index or key.
#==========================================================================================================
#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
#==========================================================================================================
#Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
#==========================================================================================================
#Set Items - Data Types
#Set items can be of any data type:
#==========================================================================================================
#A set cant contain different data types in one set
set1 = {"abc", 34, True, 40, "male"} # IMPOSIBLE
#==========================================================================================================
#It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#==========================================================================================================
#Set items are unchangeable, but you can remove items and add new items.





