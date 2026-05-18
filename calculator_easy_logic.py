import art

# basic arithmetic functions: each takes two numbers and returns the result
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

# map operator symbols to the corresponding function for easy dispatch
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
# new calculator function to encapsulate the calculator logic
def calculator():
    # print the ASCII/art logo at the start of the calculator session
    print(art.logo)

    # control variable for the main loop; when False the loop will stop
    should_add_up = True

    # prompt the user for the initial first number (start of a calculation)
    num1 = float(input("What is the first number?: "))

    # main calculation loop: runs while the user wants to continue
    while should_add_up:
        # display available operation symbols to the user
        for symbol in operations:
            print(symbol)

        # ask the user to pick an operation symbol (e.g. +, -, *, /)
        operation_symbol = input("Pick an operation (+, -, *, /): ")

        # ask for the second number for the current operation
        num2 = float(input("What is the second number?: "))

        # compute the answer by calling the function mapped to the chosen symbol
        answer = operations[operation_symbol](num1, num2)

        # show the operation and result to the user
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # ask the user what they want to do next:
        # 'y' -> continue with the current result as the new first number
        # 'n' -> start a new calculation (re-prompt for first number)
        # 'q' -> quit the calculator
        choice = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation or type 'q' to exit: ")

        if choice == 'y':
            # continue chaining calculations: set num1 to the last answer
            num1 = answer
        elif choice == 'n':
            # clear the screen visually (many newlines) and ask for a fresh first number
            print("\n" * 50)
            num1 = float(input("What is the first number?: "))
        elif choice == 'q':
            # stop the loop and say goodbye
            should_add_up = False
            print("Goodbye!")
        else:
            # any other input: stop current loop and restart a fresh calculator session
            should_add_up = False
            print("\n" * 20)
            calculator()

    # call the calculator function at module level to start the program
    calculator()



