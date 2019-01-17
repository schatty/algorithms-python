# python3
"""
Test of the coursera submission process.
"""


def sum_two(a, b):
    return a + b


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(sum_two(n, m))