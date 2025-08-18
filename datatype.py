'''x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType	

Setting the Specific Data Type
If you want to specify the data type, you can use the following constructor functions:

Example	Data Type	Try it
x = str("Hello World")	str	
x = int(20)	int	
x = float(20.5)	float	
x = complex(1j)	complex	
x = list(("apple", "banana", "cherry"))	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="John", age=36)	dict	
x = set(("apple", "banana", "cherry"))	set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	bool	
x = bytes(5)	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview
'''

x = 1   #int
y = 2.8 #float
z = 1j  #complex

print(type(x))
print(type(y))
print(type(z))

 #Float can also be scientific numbers with an "e" to indicate the power of 10.
#Floats:
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#Convert from one type to another:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#to create a random number
import random

print(random.randrange(1, 10))

#Specify a Variable Type
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
a = float(1)     # x will be 1.0
b = float(2.8)   # y will be 2.8
c = float("3")   # z will be 3.0
d = float("4.2") # w will be 4.2
e = str("s1") # x will be 's1'
f = str(2)    # y will be '2'
g = str(3.0)  # z will be '3.0'

#string
print("hello")

#quotes inside quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#assign string to a variable
a = "Hello"
print(a)

#You can use three double quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#string as array
a = "Hello, World!"
print(a[1])

#Loop through the letters in the word "banana":
for x in "banana":
  print(x)

#The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

#Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

#Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)

#print only if "expencive" is not present
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#slicing
#Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])

#slice from the start
#Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])

#slice to the end
#Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])

#negative indexing
#Use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
print(b[-5:-2])

#upper case
#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

#lower case
#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

#remove whitespace
#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Replace String
#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

#split string
#The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#string concatenation
#Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)

#To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

