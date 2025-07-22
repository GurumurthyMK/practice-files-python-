#
# Write a function that returns the sum of even numbers in a list.

def eve_sum(num_list):
    eve_sum = sum(int(x) for x in num_list if x % 2 == 0)
    print("the sum of all even digits are: ", eve_sum)

def odd_sum(num_list):
    odd_sum = sum(int(x) for x in num_list if x % 2 != 0)
    print("the sum of all odd digits are: ", odd_sum)

def get_numlist():
    usr_list = input("Enter the integers of list each value separated by space: ")
    num_list = [int(x) for x in usr_list.split()]
    ch = input("do you want the Even sum or Odd sum(Eve/Odd)?: ")
    ch = ch.strip().title()
    if ch == "Eve":
        eve_sum(num_list)
    elif ch == "Odd":
        odd_sum(num_list)
    us_ag = input("do you want to try again?: ")
    if us_ag.lower().strip() == "yes":
            get_numlist()
    else:
           print("alright bye!!")

get_numlist()