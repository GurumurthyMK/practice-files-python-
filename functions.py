#these are functions - re usable code block performing a task or a function

# this function dosent take input arg but is explicitly mentioned
def welcome(name="Default"):
    return f"Howdy!! {name}"
print(welcome("Sunil"))

# this an example function of taking user input
def greet():
    name = input("Enter your name: ")
    print("Howdy, ",name)
greet()

#Decorators
def decorator_name(func):
    def wrapper():
        print("this happens before function")
        func()
        print("this happens after the function")
    return wrapper

@decorator_name
def func():
    print("this is some function")

func()


#generators
def count(n):
    n = 1
    while n <=10:
        yield n
        n += 1
my_gen = count(7)
for i in my_gen:
    print(i)



#lambda
demo = lambda x: x+2
print(demo(10))
