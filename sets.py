#	1.	Remove duplicates from a list using a set.
my_list = ['hello', 'world', 'greetings', 'everyone', 'hello']
uniq_list = list(set(my_list))
my_list = uniq_list
print(uniq_list)

#	2.	Find the common elements between two lists using sets.
list_1 = ['1', '2', '3', '4', '5']
list_2 = ['6', '7', '8', '9', '10']
common_elements = list(set(list_1) & set(list_2))
print("the common elements are ", common_elements)

#	3.	Check if a given set is a subset of another.
main_set = set(['one','two','three'])
sub_set = {1,'one',2 , 'three'}
if sub_set.issubset(main_set):
    print("sub_set is sub set of main")
elif main_set.issuperset(sub_set):
    print("mainset is the super set of sub_set")
else:
    print("nothing to show!")

#	4.	Find the union and intersection of two sets.
inter_set = main_set ^ sub_set
un_set = main_set.union(sub_set)
print(inter_set)
print(un_set)
