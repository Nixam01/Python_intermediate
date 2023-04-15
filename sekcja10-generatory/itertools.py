import itertools as it

mylist = ['a', 'b', 'c', 'd', 'e']

for combination in it.combinations_with_replacement(mylist, 3):
    print(combination)