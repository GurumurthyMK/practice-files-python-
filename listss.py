# these are methods on lists
# lists are mutable,ordered and dynamic

#- list constructors
my_list = ['apple','banana','watermelon','jackfruit']
my_list2 = list(('name','age','ph_no','college'))
print(my_list)
print(my_list2)

#indexes
print(my_list[1:4])
#updating indexes
my_list[2] = 'berrys'
print(my_list)

# checking membership
print('berrys' in my_list)
print('watermelon' not in my_list)

# list copying
new_list = my_list.copy()
print(new_list,"this is a copied list of my_list")

# major list methods
# append method
my_list.append('guava')
print(my_list)

#exted method
all_list = []
all_list.extend(my_list)
print(all_list)

#insert method (to insert to a specific place)
all_list.insert(0, "inserted-element")
print(all_list)

#Remove method
all_list.remove('apple')
print(all_list)

#pop method
popped_element = my_list.pop(2)
print(popped_element)

#clear
clr_lst = all_list.clear()

#misc methods
print(my_list.count('a'))
print(my_list.reverse())
print(my_list.sort())
print(min(my_list))
print(max(my_list))

# common elements and removing duplicated from lists
#finding common elements btwn 2 lists
lst1 = ['one','two','three','four']
lst2 = ['three','four','five','six']
set1 = set(lst1)
set2 = set(lst2)
comm_ele = list(set.intersection(set1, set2))
print(lst1,lst2,comm_ele," the last list is common elements")

# removing duplicates
d_lst = [1,2,1,2,2,1,2,3,3,4,5,5,6,7,8,9,10,10]
print(d_lst)
set3 = set(d_lst)
d_lst = list(set3)
print(d_lst," this is the list without duplicates")
