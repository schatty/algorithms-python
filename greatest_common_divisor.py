#python3
"""
Algorithm for finding the greatest common divison of two numbers
"""
from random import randint
from stress_test import stress_test


def naive_gcd(a, b):
    best = 1
    for d in range(1, min(a, b)):
        if a % d == 0 and b % d == 0:
            best = d
    return best


def euclid_gcd(a, b):
    if b == 0:
        return a
    a_prime = a % b
    return euclid_gcd(b, a_prime)


if __name__ == "__main__":
    # Sample 1
    assert euclid_gcd(18, 35) == 1, "Sample 1 is Wrong"

    # Sample 2
    assert euclid_gcd(28851538, 1183019), "Sample 2 is Wrong"

    def arg_gen():
        return randint(2, 100), randint(2, 100)
    stress_test(euclid_gcd, naive_gcd, arg_gen, 10)