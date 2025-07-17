# This is a simple calC which will do basic math operations

import math

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def cal_c():
    print("Welcome to the simple calculator program!")
    num1 = get_int("Enter the first number: ")
    num2 = get_int("Enter the second number: ")

    print("Enter the choice of operation you want to perform:")
    print("\t1. Add")
    print("\t2. Subtract")
    print("\t3. Multiply")
    print("\t4. Divide")
    print("\t5. Square root")
    opr_ch = input("Your choice (1/2/3/4/5): ").strip()

    if opr_ch in ['1', '1.add', 'add']:
        print(f"The result is {num1 + num2}!")
    elif opr_ch in ['2', '2.subtract', 'subtract']:
        print(f"The result is {num1 - num2}!")
    elif opr_ch in ['3', '3.multiply', 'multiply']:
        print(f"The result is {num1 * num2}!")
    elif opr_ch in ['4', '4.divide', 'divide']:
        if num2 == 0:
            print("Cannot divide by 0.")
        else:
            print(f"The result is {num1 / num2}!")
    elif opr_ch in ['5', '5.square root', 'square root', 'sqrt']:
        print(f"The square roots are: sqrt({num1}) = {math.sqrt(num1):.3f}, sqrt({num2}) = {math.sqrt(num2):.3f}")
    else:
        print("Operation failed. Try again!")

def greet_usr():
    name = input("Enter your name: ")
    while True:
        ch_pr = input("Do you want to use the calc app? (Yes/No): ").strip().lower()
        if ch_pr == 'yes':
            cal_c()
        else:
            print("Good bye!")
            break

greet_usr()
