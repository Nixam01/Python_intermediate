import math

import itertools as it

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'H']
counter = 0
for combination in it.permutations(notes, 4):
    counter += 1
    print(combination)

print(counter)

print("4-notes melody, notes cannot repeat - it is variation without repeating - there are {} possibilities".format(math.factorial(len(notes)) / math.factorial(len(notes) - 4)))

input('Press enter')
counter = 0
for x in it.product(notes, repeat=4):
    counter += 1
    print(x)

print(counter)

print("4-notes melody, notes cannot repeat - it is variation with repeating - there are {} possibilities".format(pow(len(notes), 4)))