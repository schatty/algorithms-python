"""
Given array of size n with natural number count number of pairs of indices such that
1 <= i < j <= n, A[i] > A[j]. Such pair is called an inversion and shows degree
of chaos in array.
"""

from math import floor

# Correct version but too slow
def calc_with_insertion_sort(a):
    n = 0
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j-1]:
            tmp = a[j]
            a[j] = a[j-1]
            a[j-1] = tmp
            j -= 1
            n += 1
    return n


def merge(a, b):
    i_a = 0
    i_b = 0
    n_inv = 0
    merged = []
    while i_a != len(a) and i_b != len(b):
        if a[i_a] > b[i_b]:
            n_inv += len(a) - i_a
            merged.append(b[i_b])
            i_b += 1
        else:
            merged.append(a[i_a])
            i_a += 1
    if i_a == len(a):
        merged += b[i_b:]
    elif i_b == len(b):
        merged += a[i_a:]
    return merged, n_inv


def merge_sort(a, l, r):
    if r - l == 1:
        return [a[l]], 0
    m = floor((l+r)/2)
    first, n_inv_l = merge_sort(a, l, m)
    second, n_inv_r = merge_sort(a, m, r)
    merged, n_inv = merge(first, second)
    return merged, n_inv + n_inv_l + n_inv_r



def test(foo):
    data = [
    [[10, 8, 6, 2, 4, 5], 12],
    [[1, 9, 8, 1, 4, 1], 8],
    [[6, 5, 8, 6, 0, 4], 10],
    [[6, 2, 3, 7, 5, 8], 4],
    [[6, 4, 5, 0, 0, 2], 11],
    [[8, 9, 10, 7, 4, 0], 12],
    [[10, 9, 3, 8, 3, 10], 8],
    [[9, 10, 9, 5, 7, 7], 10],
    [[9, 5, 8, 9, 4, 10], 6],
    [[5, 7, 0, 2, 2, 0], 10]
    ]
    for (x, y) in data:
        assert foo(x, 0, len(x))[1] == y, f"Wrong case: For {x} expected {y}, got {foo(x)}"


if __name__ == "__main__":
    test(merge_sort)
