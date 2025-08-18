# class Bas_Car:
#    def __init__(self, model, color, engine, speed_limit):
#        self.model = model
#        self.color = color
#        self.engine = engine
#        self.speed_limit =int(speed_limit)

#    def __str__(self):
#      return  f"the base car at {self.engine}"

# car2 =Bas_Car("maruti800", "black", "basic_engine","220" )
# car1 =Bas_Car("maruti", "white","basic_engine", 200)
# car2 = car1
# print(car1.speed_limit, car2.speed_limit)
# print(car1, car2)
# print(type(car1.speed_limit))
# print(type(car2.speed_limit))


# class DateOfBirth:
#     def __init__(self, day, month, year):
#         self.day = int(day)
#         self.month = int(month)
#         self.year = int(year)

#     def __repr__(self):
#         return f"{self.day:02d}-{self.month:02d}-{self.year}"
    
# class myclass :
#     def __init__(self, name, clases, roll_number, date_of_birth:DateOfBirth ):
#         self.name = name
#         self.clases = int(clases)
#         self.roll_number = int(roll_number)
#         self.date_of_birth =date_of_birth

# student1 = myclass("Rahul", 1, 1001, DateOfBirth(29, 9, 2005))
# student2 = myclass("Shivam", 3, 1002, DateOfBirth(12, 1, 2003))  # Default month if missing
# student3 = myclass("Rohit", 3, 1003, DateOfBirth(9, 9, 2003))

# print(student1.date_of_birth.day)
# print(student2.date_of_birth.month)
# print(student3.date_of_birth)

# from datetime import datetime

# class car_brand:
#     def __init__(self,brand_name,launched,number_of_cars):
#         self.brand_name =brand_name
#         self.launched = datetime.strptime(launched,"%d-%m-%Y")
#         self.number_of_cars =int(number_of_cars)

#     def __str__(self):
#      return f"{self.brand_name}, {self.launched.date()}, {self.number_of_cars}"

# car1 = car_brand("maruti_suzuki", "24-2-1981", 17)
# car2 = car_brand("hyundai", "29-12-1967", 14)
# car3 = car_brand("tata_motors" , "1-1-1945", 16)
# car4 = car_brand("mahindra", "2-10-1945", 15)
# car5 = car_brand("BNW", "1-1-1916", 21)

# print(car1)
# print(car2)
# print(car3)
# print(car4)
# print(car5)

# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(xyz):
#     print("Hello my name is " +xyz.name)

# p1 = Person("John", 36)
# p1.myfunc()

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)

# x = Student("Mike", "Olsen")
# x.printname()

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname, fathername):
#     Person.__init__(self, fname, lname)
#     self.fathername = "karamchand"

#   def hello (self):
#     print(self.firstname,self.lastname,"Name of the father is ", self.fathername)


# x = Student("Mike", "Olsen","gurpreet")
# x.hello()
# print(x.fathername)

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     if self.a <= 20:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#   print(x)

# class vehicle:
#     def __init__(self,brandname,colour):
#         self.brandname = brandname
#         self.colour = colour
#         return
#         print("move")

# class car :
#     def __init__(self,barndname,colour):
#         self.brandname = barndname
#         self.colour = colour
#         return

#     def move(self):
#         print("move")

# class boat:
#     def __init__(self,brandname,colour):
#         self.brandname = brandname
#         self.colour = colour
#         return

#     def move(self):
#         print("sail")

# class plane:
#     def __init__(self,brandname,colour):
#         self.brandname =brandname
#         self.colour = colour
#         return

#     def move(self):
#         print("fly")


# car1 = car("maruti","white")
# boat1 = boat("Ibiza","red")
# plane1 = plane("Boeing","red and white")

# print(car1)
# print(boat1)
# print(plane1)

class Vehicle:
    def __init__(self, brandname, colour):
        self.brandname = brandname
        self.colour = colour

    def __str__(self):
        return f"{self.brandname} ({self.colour})"


class Car(Vehicle):
    def move(self):
        print("move")


class Boat(Vehicle):
    def move(self):
        print("sail")


class Plane(Vehicle):
    def move(self):
        print("fly")


car1 = Car("Maruti", "white")
boat1 = Boat("Ibiza", "red")
plane1 = Plane("Boeing", "red and white")

print(car1)
print(boat1)
print(plane1)

car1.move()
boat1.move()
plane1.move()


class person:
    def __init__(self,personname,fathername,roll_no,age):
        self.personname = personname
        self.fathername = fathername
        self.roll_no = roll_no
        self.age = age

    def printme(self):
            print(self.personname,self.fathername,self.roll_no,self.age)

person = person()