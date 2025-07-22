# 2.	Swap Tuple Elements
usr_input = input("enter the numbers for the tuples, separated by comma each : ")
tup = tuple(int(x) for x in usr_input.split(','))
swap_tup = tup[::-1]

print("the original tuple is:", tup)
print("the swapped tuple is: ", swap_tup)
