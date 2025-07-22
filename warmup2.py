# Remove Duplicates

us_input = input("enter the elements of a list each separated by a space: ")
user_list = [x for x in us_input.split()]
print("the entered list is: ", user_list)

#removing the duplicates
new_list = sorted(set(user_list))
print("list without duplicates: ", new_list)
