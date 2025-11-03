#these are the methods and functions which can be performed on strings
# strings are immutable,idenxed and iterable
#declaring example strings
f_name = "Guru"
l_name = "MK"
m_name = """I dont
            have any"""

#indexing can be done to figure out respective elements
ex_name = f_name[0:3]
print(ex_name)
#string reversal can be done by using [::-1] index
print(f_name[::-1])

# the len() method - gives string length
print(len(ex_name))

#slicing of string
ex_slice = f_name[1:3]
print(ex_slice)

#repeating of a string
print(l_name*2)

#concatenating two strings
print(f_name+l_name)

#These are membership methods
if "G" in f_name:
    print("true and found")
elif "H" not in f_name:
    print("yes not found")
else:
    print("none")

# other misc string methods
eg_str = "Alphabet"
egl = eg_str.lower()
print(egl)
egu = eg_str.upper()
print(egu)
m_nameT = m_name.title()
print(m_nameT)
egC = eg_str.capitalize()
print(egC)
egSC = eg_str.swapcase()
print(egSC)

# some modification methods
#find method
print(f_name.find("G"))

#replace method
rep_str = f_name.replace("G", "S")
print(rep_str)

#split method
sl_str = "1,2,3,4"
s = sl_str.split(",")
print(s)
#join method
s = str(s)
j = s.join(",")
print(j)

#other misc methods
e_str = "name"
print(e_str.endswith("e"))
print(e_str.isalpha())
print(e_str.isalnum())
print(e_str.isdigit())
