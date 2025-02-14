# here I start a iterators
a = "Belk"
x = iter(a)
print(next(x))
print(next(x))
print(next(x))
print(next(x))




# so how we see we can iterate with some function 
# __next__() 
# __iter__()

print(next(iter(a))) 

#The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
#To prevent the iteration from going on forever, we can use the StopIteration statement.
#In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
