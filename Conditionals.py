#these are the conditional statements
#if else, elif and if elif else

name = 'Akash'
age = int(input("Enter you age: "))
if age >=18 and age < 120:
    print(f'you can vote {name}')
elif age < 18:
    print('invalid age for voting')
else:
    print('Invalid input, please enter a proper age')
