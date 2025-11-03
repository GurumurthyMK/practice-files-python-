# these are the different data types available in python

# numeric data types:
integer_whole_number = int(123)
decimal_number = float(23.452)
complex_number_imaginary = complex(34+3j)

print(type(integer_whole_number))
print(type(decimal_number))
print(type(complex_number_imaginary))

#boolean data types
yes = True
no = False
print(type(yes))
print(type(no))

#None type data type
var_name = None
print(type(None))

#Sequence data types
#String (immutable)
str_name = "this is a string element, a sequence of character"
print(type(str_name))

#list (mutable)
listt_name = ['Dog','cat','parrot','lion','tiger']
print(type(listt_name))

#tuple (immutable)
tupple_name = ('Ichigo', 'aizen', 'yamato','soulking')
print(type(tupple_name))

#sets (set=mutable, frozen set=immutable)
sett_name = {'hey', 'hello','hey','howdy','good'}
print(type(sett_name))
frozensett = frozenset(sett_name)
print(type(frozensett))

#dictionary (mutable)
dict_name = {'Name': 'Guru','Age': 19}
print(type(dict_name))
