'''
source = "reportLine += 1"
reportLine = 0
exec(source)
print(reportLine)

sourceCompiled = compile(source, 'internal variable source', 'exec')
exec(sourceCompiled)

print(reportLine)

import time
start = time.time()

for i in range(10000):
    exec(source)

stop = time.time()
time_not_compiled = stop - start
start = time.time()

for i in  range(10000):
    exec(sourceCompiled)

stop = time.time()
time_compiled = stop - start
print(time_not_compiled)
print(time_compiled)
print(time_not_compiled/time_compiled)
'''
import math
import time
formulas_list = ["abs(x**3 - x**0.5)","abs(math.sin(x) * x**2)"]
argument_list = []
for i in range (1000):
    argument_list.append(i/10)

for formula in formulas_list:
    results_list = []
    print(formula)
    start = time.time()
    for x in argument_list:
        results_list.append(eval(formula))
        print(eval(formula))
        print("wartosc minimalna ", min(results_list))
        print("wartosc maksymalna ", max(results_list))
    stop = time.time()
    time_not_compiled = stop - start
    print("czas trwania obliczen ",time_not_compiled)

argument_list = []
for i in range (1000):
    argument_list.append(i/10)


for formula in formulas_list:
    results_list = []
    print(formula)
    start = time.time()
    compiled_formula = compile(formula, 'internal variable source', 'exec')
    for x in argument_list:
        results_list.append(eval(compiled_formula))
        print(eval(compiled_formula))
        print("wartosc minimalna ", min(results_list))
        print("wartosc maksymalna ", max(results_list))
    stop = time.time()
    time_not_compiled = stop - start
    print("czas trwania obliczen ",time_not_compiled)
