#modify string or function for str

a = "Hello, World!"
print(a.upper())

#output is:HELLO, WORLD!
#definition do upper all simvols


#==============================================================================================================================

a = "Hello, World!"
print(a.lower())
#output is:hello, world!
#definition do lower all simvols


#==============================================================================================================================

a = "      Hello, World!     "
print(a.strip()) # returns "Hello, World!"
#output is:Hello, World!
#definition Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

#==============================================================================================================================

a = "Hello, World!"
print(a.replace("H", "J"))
#output is :Jello, World!
#definition The replace() method replaces a string with another string:

#==============================================================================================================================

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
#output:['Hello', ' World!']
#definition The split() method returns a list where the text between the specified separator becomes the list items.


 