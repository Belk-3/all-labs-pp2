# very big topic in python but i know so i just write things which i dont know becouse here toooooo much or thing which is important
"" == ''
#==============================================================================================================================

#You can assign a multiline string to a variable by using three quotes:
a = """Lorem ipsum dolor sit amet,

consectetur adipiscing elit,

sed do eiusmod tempor incididunt

for example like that xDDD

ut labore et dolore magna aliqua."""
print(a)

#==============================================================================================================================

#Strings are Arrays
a = "Hello, World!"
print(a[0])

#==============================================================================================================================

#Looping Through a String
for x in "BAANAAAANAAAAAAaaa":
  print(x)

#==============================================================================================================================
  
#we use len() for find a lenght of string
a = "asdfshfsfhsafsdfsbd"
print(len(a))

#==============================================================================================================================

#we also can use string as a boolean
a = "The best things in life are free!"
print("free" in a)
#or like that
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")