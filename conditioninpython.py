#age
age = int(input("enter your age:"))

if age < 0:
    print("please enter a valid age ")
elif age <18:
    print("you are a minor because your age is ",age)
elif age <25:
    print("you are adult because your",age)    
elif age <27:
    print("you are eligible for marrige because your age is ",age)
elif age >38:
    print("you are a senour citizen because your age is 24",age)
else:
    print("you are getting old")

 # taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
 
# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)

colour = input("enter colour name: ")
print(colour)

#number
number = input("enter a valid number")

#split
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)

#global
x= 5;
y= 7;
z= 8;
  
def myfunc1():
  
  print("value z",z)
  y= z;
  print("value y",y)

myfunc1()

print("value y",y)
print("value z1",z) 


#name
name = input("Enter your name")
print("welcome", name,"how are you")
#health
reply = input("reply")
print("it's good to hear that")


# 3 pairs
def get_inputs():
    a, b, c = input("type three best friend ").split()
    return a, b, c

a ,b ,c , = get_inputs()
print("your 1 friend =", a)
print("your 2 friend =", b)
print("your 3 friend =", c)

# Taking input as int
# Typecasting to int
n = int(input("How many roses?: "))
print(n)

# Taking input as float
# Typecasting to float
price = float(input("Price of each rose?: "))
print(price)
 
 #to find the type of variable
a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for":2, "Geeks":3}


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))


y= 9

def myfunc():
  return y


def myfunc1():
  return myfunc
  
z = myfunc1() #function run
print(z())



y= 9

def myfunc():
  return y


def myfunc1():
  return myfunc()
  
z = myfunc1()

print(z)



y= 9;

def myfunc():
  return y;


def myfunc1():
  return myfunc;

z = myfunc1; #function assign

print(z()());

x = 5  # Global variable

def myfunc():
    global x     # Tell Python you want to use the global x
    x = 10       # This modifies the global x

myfunc()
print(x)         # Output: 10

x = "Hello World"
x1 = 20
x2 = 20.5
x3 = 1j
x4 = ["apple", "banana", "cherry"]
x5 = ("apple", "banana", "cherry")
x6 = range(6)
x7 = {"name" : "John", "age" : 36}
x8 = {"apple", "banana", "cherry"}
x9 = frozenset({"apple", "banana", "cherry"})
x10 = True	
x11 = b"Hello"
x12 = bytearray(5)
x13 = memoryview(bytes(5))	
x14 = None
print(type(x))
print(type(x1))
print(type(x2))
print(type(x3))
print(type(x4))
print(type(x5))
print(type(x6))
print(type(x7))
print(type(x8))
print(type(x9))
print(type(x10))
print(type(x11))
print(type(x12))
print(type(x13))
print(type(x14))

x = 9    # int
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

#pridict number
import random

print(random.randrange(1, 10))

print("pridict the number in my mind")

number = int(input("number in your mind"))
import random

print("the number in my mind",random.randrange(1, 10))

#array in string
a = "Hello, World!"
print(a[12])

#loop in string
x = 1
while x <= 5:
    print(x)
    x += 1

for i in range(5):
    print(i)

#lenght of a srting
a = "Hello, World!"
print(len(a))

print =input("enter 5 element of life")
text =input
if "water" not in text:
   print = ("no, answer is wrong")

   number = input("enter a valid number")

if number (len(11)):
    print("please enter a valid number")
elif number== 9041142178:
    print("please dismental your number")
elif number == 8194994419:
    print("Please dismantle your number")
else:
     print(number,"is confirmed")