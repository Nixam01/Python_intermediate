'''
var_x = 10
password = 'My super secret password'
#globall = globals().copy()
#del globall['password']
source = 'password'

globals = {}

#source = '__import__("os").getcwd()'

result = eval(source, globals)
print(result)

'''

import math

argument_list = []
for argument in range (100):
    argument_list.append(argument/10)
print("podaj wzor")
formula = input()

for x in argument_list:
    result = eval(formula)
    print(result)

