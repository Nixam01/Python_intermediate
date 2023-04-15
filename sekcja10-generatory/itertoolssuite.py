import itertools

cars = ['BMW', 'Fiat', 'Toyota']
selections = [True, False, True]
result = itertools.compress(cars, selections)
for each in result:
    print(each)


#zip_longest --> łączy 2 liste w 1 tuple i wypełnia wartosci parametrem fill value

