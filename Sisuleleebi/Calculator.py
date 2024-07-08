def add (n1, n2):
    return n1 + n2

def subtract (n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

operations = { "+": add, "-": subtract,
               "*": multiply, "/": divide}
def calculator():
    num1 = float(input("Enter the first number: "))
    resume = True
    while resume == True:
            for symbols in operations:
                print(symbols)
            operation = input("Enter the operation: ")
            num2 = float(input("Enter the second number: "))
            function = operations[operation]
            answer = function(num1, num2)

            print(f"{num1} {operation} {num2} = {answer}")

            if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start new calculation.").lower() == "y":
                num1 = answer
            else:
                print("Here we go1")
                resume = False
                calculator()

calculator()