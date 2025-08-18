print("hello! how are you")

#python syntax
if 5 > 2:
    print("five is greater than two")
    #leave the space at the start called as indentation


if 5 > 2:
 print("Five is greater than two!")
 print("Five is greater than two!")
#leave same number of block in the same block of code

#python variable
x = 5
y ="hello how are you"
print(x)
print(y)

'''this is used to make comment 
written in more than just one line'''

#creating variable 
x = 5
y = "John"
print(x)
print(y)
# variable are x and y that are assign by 5 and john

#assigning data type int and str to the varable
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
#the python will make the new assigned value as priorty

#casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#casting is used to specify the data type of a variable

#get the type
x = 5
y = "John"
print(type(x))
print(type(y))
#it is used to get the data type of a variable

#case-sensitive 
a = 4
A = "Sally"
#A will not overwrite a

#legal variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#some illegal variable names
#2myvar = "John"
#my-var = "John"
#my var = "John"

#three different type of case
#camel case
#pascal case
#snale case

#many value to multiple variable
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#one value to multiple value
x = y = z = "Orange"
print(x)
print(y)
print(z)

#unpack a collection 
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#output variable
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#for variable
x = 5
y = 10
print(x + y)

#an variable and integer can't be put together with + sign
#so comma is used
x = 5
y = "john"
print(x, y)

#gloabal variable
#Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''

#getting the data type
x = 5
print(type(x))

