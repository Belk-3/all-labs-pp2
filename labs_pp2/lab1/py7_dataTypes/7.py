q = "hello"                         # str
w = 5                               # int
e = 20.1                            # float
r = 1j                              #complex
t = ["a","b","c"]                   #list
y = ("a","b","c")                   #tuple
u = range(6)                        #range
i = {"name" : "John","age" : 36}    #dict
o = {"a","b","c"}                   #set
p = frozenset({"a","b","c"})        #frozenset
a = True                            #bool
s = b"Hello"                        #bytes
d = bytearray(5)                    #bytarray
f = memoryview(bytes(5))            #memoryview
g = None                            #NoneType
print(q,w,e,r,t,y,u,i,o,p,a,s,d,f,g)

q = str("hello")                         # str
w = int(5)                               # int
e = float(20.1)                            # float
r = complex(1j)                              #complex
t = list(("a","b","c"))                   #list
y = tuple(("a","b","c"))                   #tuple
u = range(6)                        #range
i = dict({"name" : "John", "age" : 36})    #dict
o = set({"a","b","c"})                   #set
p = frozenset({"a","b","c"})        #frozenset
a = bool(5)                            #bool
s = bytes(5)                        #bytes
d = bytearray(5)                    #bytarray
f = memoryview(bytes(5))            #memoryview

print(q,w,e,r,t,y,u,i,o,p,a,s,d,f)


#-----------------------------------------------------------------
#to get a date type we use this
x = 5
print(type(x))