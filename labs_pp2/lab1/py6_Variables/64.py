x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# here we can see that VAriable x is in function so x is local variable becouse its in functon
# so based on this we can say that we have two typess of variable LOCAL and GLOBAL



def myfunc():
  global x
  print("Python is " + x)

myfunc()
print(x)
# here we can see that in function and out of the function we have value of x becouse we used a GLOBAL function which means that our X is global xD
