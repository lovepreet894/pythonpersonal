def add(x, y):
    print(f"Result = {x + y}")

def multiply(x, y):
    print(f"Result = {x * y}")

def minus(x, y):
    print(f"Result = {x - y}")

def divide(x, y):
    if y != 0:
        print(f"Result = {x / y}")
    else:
        print("Error: Cannot divide by zero")

def calculator():
    print("Welcome to my computer calculator")

    operations = {
        1: ("Add", add),
        2: ("Multiply", multiply),
        3: ("Subtract", minus),
        4: ("Divide", divide)
    }

    while True:
        print("\nHere are the options for you to select:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name} the 2 numbers")

        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            choice = int(input("Enter your choice (1-4): "))

            operation = operations.get(choice)
            if operation:
                _, func = operation
                func(x, y)
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")

        again = input("\nDo you want to perform another operation? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

# Run the calculator
if __name__ == "__main__":
    calculator()
