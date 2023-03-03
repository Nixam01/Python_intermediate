import functools
import smtplib
import time

@functools.lru_cache(maxsize=100)
def fib(n):
    if n < 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result

for a in range(1, 30):
    start = time.time()
    result = fib(a)
    stop = time.time()
    print("Iteration {} Fibonacci {} Time {}".format(a, result, stop - start))

print(fib.cache_info())