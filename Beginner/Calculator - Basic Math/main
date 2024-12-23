#importing logo from art.py file
import art

#mathematic functions
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

#operations
keys = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

#gets inputs needed from users to calculate result & recursively asks if user want to keep calculating or not
def calculate():
    print(art.logo)
    calc_again = True
    num1 = float(input("What is the first number?: "))

    while calc_again:
        for i in keys:
            print(i)
        key_choice = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))

        result = (keys[key_choice](num1, num2))
        print(f"{num1} {key_choice} {num2} = {result}")

        yes_or_no = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        while yes_or_no == 'n':
            calc_again = False
            print("\n" * 50)
            calculate()
        num1 = result

calculate()
