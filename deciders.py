# break, continue and pass
#continue skips the instant element
for i in range(10):
    if i == 8:
        continue
    print(i)

#break - breaks out of the loop running
while True:
    print("this won't print again")
    break

# pass is to just pass that instance of code without doing anything
for i in range(10):
    pass
print("this is a for loop of range 10 - but doesn't do anything")
