from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator () :
    print(logo)
    num1 = float(input("What's the first number?\n"))
    num2 = float(input("What's the second number?\n"))

    for operation in operations: 
        print(operation)

    operation_symbol = input("Pick an operation from the line above: ")

    operation_function = operations[operation_symbol]

    answer = operation_function(num1 , num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    should_continue = True
    while should_continue :
        is_continue = input("Type 'y' to continue calculating with 8, or type 'n' to exit .: \n")
        if is_continue == "y":
            operation_symbol = input("Pick an operation : \n")
            num1 = answer
            num2 = float(input("What's the next number? \n"))

            operation_function = operations[operation_symbol]
            answer = operation_function(answer , num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")
        else:
            should_continue = False
            calculator()

calculator()
