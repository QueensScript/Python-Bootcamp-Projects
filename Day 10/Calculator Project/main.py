def add(n1, n2):
    return n1 + n2

def subtract (n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

from art import logo


while True:
    print (logo)
    n1 = float(input("Please type the first number.\n"))
    continue_calculate = True
    while continue_calculate:
        select_operator = input("Please select the mathematical operator:\n+\n-\n*\n/\n")
        n2 = float(input("Please type the second number.\n"))
        result = operations[select_operator](n1, n2)

        print(f"{n1} {select_operator} {n2} = {result}")

        cycle = input(f"Type 'y' to continue calculating with {result} or type 'n' to begin a new calculation: ")

        if cycle == "y":
            n1 = result
        else:
            continue_calculate = False
            print("\n" * 20)
