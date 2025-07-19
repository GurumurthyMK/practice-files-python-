#	1.	Convert a list to a tuple and back.
my_list = ['1', '3', '2', '4', '1']
my_tuple = tuple(my_list)
print(my_tuple)
#cpverting a tuple to a list
sec_tuple = ('area', 'square', 'perimeter', 'volume')
sec_list = list(sec_tuple)
print(sec_list)


#	2.	Create a tuple of 5 values and unpack them into variables.
measure1, measure2, measure3, measure4 = sec_tuple
print(measure1,measure2,measure3,measure4)

#	3.	Given a tuple of numbers, find the max and min values without using max() or min().
print(my_tuple)
min_value = my_tuple[0]
max_value = my_tuple[0]

for num in my_tuple:
    if min_value > num:
        min_value = num
    if max_value < num:
        max_value = num
print("the min value is ", min_value)
print("\nthe max value is, ", max_value)
