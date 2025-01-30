#Loop Through a Tuple
# we can do it with for or while as a list
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


#Join Tuples
# with + or *
  
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)


#count()	#Returns the number of times a specified value occurs in a tuple
#index()	#Searches the tuple for a specified value and returns the position of where it was found