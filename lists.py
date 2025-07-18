# 1.Create a list of 10 numbers. Reverse it without using reverse(). 
my_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
print(my_list)
my_list = my_list[::-1]
print(my_list)

# 2.	Remove all even numbers from a list.
my_list = [x for x in my_list if int(x)%2 !=0]
print(my_list)  

# 3.	Find the second largest number in a list.
int_list = [int(x) for x in my_list]
uniq_list = list(set(int_list))
uniq_list.sort()
if len(uniq_list) >= 2:
    print("the second largest integer is,", uniq_list[-2])
else:
    print("it dosen't have enough integers!")


# 4.	Write a function that flattens a nested list like [1, [2, [3, 4]], 5].
def flatten_list(nested_lists):
    flat = []
    for items in nested_lists:
        if isinstance(items, list):
            flat.extend(flatten_list(items))
        else:
            flat.append(items)
    return flat

nested = ['2', '2334',['23'],'234',['234']]
print(flatten_list(nested))