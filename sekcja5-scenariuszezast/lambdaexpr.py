def double(x):
    return x * 2

x = 10
x = double(x)
print(x)
print('*'*30)

x = 10
f = lambda x: x * 2
print(f(x))

print('*'*30)


def mk_thg(a, b, c):
    if c > 0:
        return lambda a, b: a + b
    else:
        return lambda a, b: -a - b


p = mk_thg(1, 2, 1)
print(p(3,4))

print('*'*30)

text_list = ['x','xxx','xxxxx','xxxxxxx','']

f = lambda x: len(x)
print(f(text_list[1]))

newlist = list(map(f, text_list))
print(newlist)
print(list(map(lambda s: len(s), text_list)))