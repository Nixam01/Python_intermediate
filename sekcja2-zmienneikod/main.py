myvar = 'Hello Pycharm!'
myvar2 = myvar + '!!'
print(myvar2, myvar)
print(type(myvar), type(myvar2))
print('Are the variables the same?', myvar is myvar2)
print(id(myvar), id(myvar2))
myvar2  = myvar2[:-2]
print('Is value the same?', myvar == myvar2)
print(id(myvar), id(myvar2))

a = b = c =10
print(a, b, c)
print(id(a), id(b), id(c))
a = 20
print(a, b, c)
print(id(a), id(b), id(c))
a = b = c = [1,2,3]
a = a.append(4)
print(a, b, c)
print(id(a), id(b), id(c))

x = 10
y = 10
print(id(x), id(y))

y = y + 1 - 1
print(id(x), id(y))

y = y + 1234567890 - 1234567890
print(id(x), id(y))
