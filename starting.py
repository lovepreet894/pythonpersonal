#x = "awesome"
 
def myfun ():
   global x
   x = "good"
   print("python is", x )
myfun()

print("python is", x )