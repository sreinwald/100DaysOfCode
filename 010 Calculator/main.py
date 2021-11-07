# create a calculator that can add, subtract, multiply and divide


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculator():
    first_number = float(input("Please enter your first number: "))
    operator = input("Please enter the operator you would like to use:\n+\n-\n/\n*\n")
    second_number = float(input("Please enter your second number: "))

    if operator == "+":
        result = add(first_number, second_number)
    elif operator == "-":
        result = subtract(first_number, second_number)
    elif operator == "*":
        result = multiply(first_number, second_number)
    elif operator == "/":
        result = divide(first_number, second_number)
    else:
        result = "Invalid operator"
    return f"{first_number}{operator}{second_number}={result}"


keep_going = True

print("Welcome to the calculator!")
while keep_going:
    print(calculator())
    keep_going = input("Would you like to continue? (y/n)")
    if keep_going == "n":
        keep_going = False
