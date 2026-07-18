import art

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(art.logo)

first_number = int(input("Enter first number: "))

calculation = True
while calculation:
    for operation in operations:
        print(operation)
    operation = input(f"Pick an operation: ")
    second_number = int(input("Enter second number: "))
    calculation = operations[operation](first_number, second_number)
    print(f"{first_number} {operation} {second_number} = {calculation}")
    user_answer = input(f"Type 'y' to continue calculating with {calculation}, or type 'n' to start a new calculation:\n")
    if user_answer == "y":
        first_number = calculation
    else:
        print(art.logo)
        first_number = int(input("Enter first number: "))




