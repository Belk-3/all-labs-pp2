# we can use a list as a loop

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#with while or for
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])