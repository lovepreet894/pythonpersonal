def add(x,y):
    print(f"Result = {x + y}")

def multiply(x,y):
    print(f"Result = {x + y}") 

def minus(x,y):
    print(f"Result = {x + y}")

def divide(x,y):
    if y != 0:
        print(f"Result = {x + y}")
    else:
        print("cannot be divided by 0")  
def clculator():
    print("welcome to my computer")

    print("""here is the options for you to select 
        1. Add the 2 numbers
        2. Multiply the 2 numbers
        3. Subtract the 2 numbers
        4. Divide the 2 numbers
    """)

    x = float(input("enter first digit"))
    y = float(input("enter second digit"))
    choice = int(input("Enter your choice (1-4): "))


    match choice :
        case 1:
            print = add(x,y)
        case 2:
            print = multiply(x,y)
        case 3:
            print = minus(x,y)
        case 4:
            print = divide(x,y)
        case _:
            print = ("invalid result")

    while true:


        firto =input("do you want to do another calculation.(yes/no)!").lower()
        if firto != 'yes':
            print("thnku for using the calculator")
            break
