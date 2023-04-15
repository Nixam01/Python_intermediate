import itertools


def get_factors(x):
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list
print('factors of 20')
print(get_factors(20))
print('liczby doskonałe \n')
candidate_list = list(range(1, 10001))
filtered_list = list(itertools.filterfalse(lambda x: x != sum(get_factors(x)), candidate_list))


for p in filtered_list:
    print(p, get_factors(p))