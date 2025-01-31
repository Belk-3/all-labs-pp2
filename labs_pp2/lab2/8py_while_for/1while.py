# With the while loop we can execute a set of statements as long as a condition is true.
# here nothing to tell

#========================================================================================
#for
#The range() function defaults to increment the sequence by 1, however it is possible to specify the
#increment value by adding a third parameter: range(2, 30, 3):
for x in range(2, 30, 3):
  print(x) 

#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#Note: The else block will NOT be executed if the loop is stopped by a break statement.


#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass