# python3
"""
Finding maximum number from set of pairwise products
"""
import random


def stress_test(n_iter=1e3):
    for i in range(n_iter):
        if i % 1e2 == 0:
            print("Processing: ", i)
        n = random.randint(2, 1e3)
        a = [random.randint(1, 1e3) for _ in range(n)]
        result_1 = max_pairwise_product(a)
        result_2 = max_pairwise_product_fast(a)
        if result_1 != result_2:
            print("Wrong Result")
            print("Input data: ", a)
            print("Expected: ", result_1)
            print("Got: ", result_2)
            break
    if i == n_iter-1:
        print("OK.")


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[first] * numbers[second])
    return max_product


def max_pairwise_product_fast(numbers):
    n = len(numbers)
    # Find maximal number
    max_i = 0
    for i in range(1, n):
        if numbers[i] > numbers[max_i]:
            max_i = i
    numbers[0], numbers[max_i] = numbers[max_i], numbers[0]

    # Find second max number
    max_i = 1
    for i in range(2, n):
        if numbers[i] > numbers[max_i]:
            max_i = i

    return numbers[0] * numbers[max_i]


if __name__ == "__main__":
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))

    # stress_test(n_iter=1000)

