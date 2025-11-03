# this is the Exception method in python - an event which interrupts the flow of a program
# the types of errors usually seen are as below

# zero division error - when tried to divide by zero
try:
    num1 = 123
    num2 = 0
    res = num1/num2
except ZeroDivisionError:
    print("cannot divide by zero")

# type error 
try:
    print(1+2+ "hi")
except TypeError:
    print("cannot add two distinct types")

# value error
try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError as e: # we can use this line of code to store and display the intrepreter error dialogue itself as output text
    print("Error, ",e)
    print("enter a valid value")

# bad usage of exception 
# dealin with all kinds of exception with one method
try:
    grade = int(input("Enter your grade: "))
    print(grade)
except Exception as m:
    print("Enter a proper grade")
    print(m)