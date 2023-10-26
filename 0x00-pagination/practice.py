# import sys


# def fibo(num):
#     if num == 0 or num == 1:
#         return 1
#     return fibo(num - 1) + fibo(num - 2)


# end = int(sys.argv[1])
# start = end - 10
# print(f'calculating fibo from {start} to end {end}')

# for x in range(start, end + 1):
#     num = fibo(x)
#     print(num)


import time
import functools


# def add(a, b):
#     time.sleep(2)
#     return a + b


# cache = {}


# def cached(a, b):
#     if (a, b) in cache:
#         return cache[(a, b)]
#     result = add(a, b)
#     cache[(a, b)] = result
#     return result


# print(cached(3, 5))
# print(cached(3, 5))
# print(cached(5, 7))
# print(cached(5, 7))

@functools.cache
def cache_math(a, b):
    time.sleep(2)

    return a + b


print(cache_math(34, 6))
print(cache_math(34, 6))
