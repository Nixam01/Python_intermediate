'''
var_x = 10
source = 'var_x + 4'
result = eval(source)
print(result)

source = 'var_x = 4'
result = exec(source)
print(var_x)

source = input("enter your expression")
print(eval(source))
'''

files_to_process = [
    r"C:\Users\marci\PycharmProjects\Python_sredniozaawansowany\sekcja3-rozbudowakodu\katalogroboczy\skrypt1.py",
    r"C:\Users\marci\PycharmProjects\Python_sredniozaawansowany\sekcja3-rozbudowakodu\katalogroboczy\skrypt2.py"
    ]

import os
for file in files_to_process:
    print(os.path.basename(file))
    with open(file, 'r') as f:
        source = f.read()
        exec(source)

