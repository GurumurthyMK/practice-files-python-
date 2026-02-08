my_dict = {x: x%2!=0 for x in range(0,100) if x > 0}
print(my_dict)

your_dict = {y: y+1 <=50 for y in range(0,50) if y%2 == 0}
print(your_dict)