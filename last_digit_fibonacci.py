#python3
"""
Algorithm for computing last digit of given fibonacci number
"""
import random
from stress_test import stress_test


def fib_last_digit_list(n):
    if n <= 1:
        return n
    n += 1
    f = [0] * n
    f[0] = 0
    f[1] = 1
    for i in range(2, n):
        f[i] = f[i-1] + f[i-2]
    return f[-1] % 10


def fib_last_digit(n):
    if n <= 1:
        return n
    f_first = 0
    f_second = 1
    f_res = f_first + f_second
    for i in range(1, n):
        if i % 1e2 == 0:
            f_first = f_first % 10
            f_second = f_second % 10
        f_res = f_second + f_first
        f_first = f_second
        f_second = f_res
    return f_res % 10


if __name__ == "__main__":
    # Sample 1
    assert fib_last_digit(3) == 2, "Sample 1 is wrong."

    # Sample 2
    assert fib_last_digit(331) == 9, "Sample 2 is wrong."

    # Sample 3
    assert fib_last_digit(327305) == 5, "Sample 3 is wrong."

    stress_test(fib_last_digit, fib_last_digit_list,
                lambda: random.randint(0, 100), n_iter=100)
