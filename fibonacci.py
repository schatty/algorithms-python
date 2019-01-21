#python3
"""
Algorithm for computing fibonacci numbers
"""
import random
from stress_test import stress_test


def fib_recurse(n):
    if n <= 1:
        return n
    return fib_recurse(n - 1) + fib_recurse(n - 2)


def fib_list(n):
    if n <= 1:
        return n
    n += 1
    f = [0] * n
    f[0] = 0
    f[1] = 1
    for i in range(2, n):
        f[i] = f[i-1] + f[i-2]
    return f[-1]


def fib(n):
    if n <= 1:
        return n
    f_first = 0
    f_second = 1
    f_res = f_first + f_second
    for i in range(1, n):
        f_res = f_second + f_first
        f_first = f_second
        f_second = f_res
    return f_res


if __name__ == "__main__":
    #stress_test(fib, fib_list, lambda: random.randint(0, 100), n_iter=100)
    n = int(input())
    print(fib(n))