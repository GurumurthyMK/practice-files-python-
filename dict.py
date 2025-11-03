#these are key value pairs
#ordered and dynamic

# operations on dictionaries
# creating a dictionary
my_dict = {
    'Name': 'Guru', 'Age': '19', 'Role': 'ML Scientist', 'Goal': 'The Greatest', 'Weakness': 'NONE'
}
print(my_dict)

# adding opr
my_dict['Idol'] = 'Marcus aurelius'
print(my_dict)

#updating opr
my_dict['Goal'] = "To be the Greatest"
print(my_dict)

#deleting opr
del my_dict['Weakness']
print(my_dict)

# methods on dictionary

#get method
role = my_dict.get('Role')
print(role)

# getting keys
keys = list(my_dict.keys())
print(keys)
#getting values
values = list(my_dict.values())
print(values)

#items method
items = list(my_dict.items())
print(items)

# pop method
popped = my_dict.pop('Idol')
print(popped)

pop_it  = my_dict.popitem()
print("the last item of the list gets popped- ", pop_it)

#clear method
clr_dict = my_dict.clear()
print("this is the cleared list - ", clr_dict)
