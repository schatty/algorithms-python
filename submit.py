#python3
"""
Algorithm for computing last digit of given fibonacci number
"""


def least_common(a, b):
    def euclid_gcd(a, b):
        if b == 0:
            return a
        a_prime = a % b
        return euclid_gcd(b, a_prime)

    gcd = euclid_gcd(a, b)
    return a * b // gcd


if __name__ == "__main__":
    a, b = list(map(int, input().split()))
    print(least_common(a, b))