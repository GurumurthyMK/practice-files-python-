#	1.	Count the frequency of characters in a string using a dictionary.
m_str = " Happy Birthday People!!"
freq = {}

for char in m_str:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1 
print(freq)

#	2.	Create a contact book using a dictionary: name as key, phone number as value.
ph_book = {}
contact_name = input("enter the contact name to be saved: ")
ph_num = input("enter the phone number: ")
inp = input("do you want to add this contact? (yes/no): ")
if inp.lower() == 'yes':
    ph_book[contact_name] = (ph_num)
    print(ph_book)
else:
    print("alright!")


#	3.	Sort a dictionary by its values.
new_dict = {'name': 'guru', 'city': 'blore', 'studying': 'true'}
sort_dict = dict(sorted(new_dict.items(), key=lambda item: item[1]))
print(sort_dict)

#	4.	Invert a dictionary (keys become values and vice versa).
dum_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5'}
# this is going to invert the keys and values 
inversed_dict = {v: k for k, v in dum_dict.items()}
print(inversed_dict)

