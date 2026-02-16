# Modules are packages/Libraries used to draw out some operation
import SIR
#Using available modules 
from math import pi 
num = int(input("Enter a number: "))
result = num*pi
print(result)
print("Above is an example of borrowing preset modules and its functions")


# using custom modules (intrest rate module)
P = 2000
I = 200
T = 1234567890142132513851
SI = SIR.simple_intrest(P,I,T)
print(SI)


