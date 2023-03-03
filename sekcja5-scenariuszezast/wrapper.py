import time
from datetime import datetime
import functools

def ChangeSalary(emp_name, new_salary, is_bonus = False):
    print('Changing Salary for {} to {} as bonus = {}'.format(emp_name, new_salary, is_bonus))
    return new_salary

print(ChangeSalary('Johnson', 20000, True))

def CreateFunctionWithWrapper(func):
    def func_with_wrapper(*args, **kwargs):
        print('_'*10)
        result = func(*args, **kwargs)
        print('+'*10)
        return result
    return func_with_wrapper

ChangeSalaryWithLog = CreateFunctionWithWrapper(ChangeSalary)

print(ChangeSalaryWithLog('Johnson', 20000, True))

print('*'*30)


def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v

def Wrapper(func):
    def func_with_wrapper(*args, **kwargs):
        start = datetime.now()
        v = func(*args, **kwargs)
        stop = datetime.now()
        timemeasured = stop - start
        print("Funkcja {} wykonana w czasie {}".format(func, timemeasured))
        return v
    return func_with_wrapper


@Wrapper
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v

print(get_sequence(3))