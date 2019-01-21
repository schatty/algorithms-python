#python3
"""
Algorithm for computing least common multiple of the two numbers
"""
from random import randint
from stress_test import stress_test


def least_common_naive(a, b):
    max_n = max(a, b)
    n = max_n
    while True:
        n += max_n
        if n % a == 0 and n % b == 0:
            break
    return n


def least_common(a, b):
    def euclid_gcd(a, b):
        if b == 0:
            return a
        a_prime = a % b
        return euclid_gcd(b, a_prime)

    gcd = euclid_gcd(a, b)
    return a * b // gcd


if __name__ == "__main__":
    # # Sample 1
    assert least_common(6, 8) == 24, "Sample 1 is wrong."
    print("Sample 1 done.")

    # # Sample 2
    assert least_common(28851538, 1183019) == 1933053046, "Sample 2 is wrong."
    print("Sample 2 done.")

    def arg_gen():
        return randint(2, 100), randint(2, 100)
    stress_test(least_common, least_common_naive, arg_gen, 10)