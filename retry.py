my_dict = {x: x!=0 for x in range(0,100) if x%2==0}
print(my_dict)

new_dict = {i: i%2!=0 for i in my_dict if i!=0}
print('\n',new_dict)