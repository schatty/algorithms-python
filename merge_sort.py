from math import floor


def merge(a, b):
    i_a = 0
    i_b = 0
    merged = []
    while i_a != len(a) and i_b != len(b):
        if a[i_a] > b[i_b]:
            merged.append(b[i_b])
            i_b += 1
        else:
            merged.append(a[i_a])
            i_a += 1
    if len(a) == 1 and len(b) == 1:
        if a[0] > b[0]:
            return [b[0], a[0]]
        else:
            return [a[0], b[0]]
    if i_a == len(a):
        merged += b[i_b:]
    elif i_b == len(b):
        merged += a[i_a:]
    return merged


def merge_sort(a, l, r):
    if r - l == 1:
        return [a[l]]
    m = floor((l+r)/2)
    first = merge_sort(a, l, m)
    second = merge_sort(a, m, r)
    merged= merge(first, second)
    return merged


if __name__ == "__main__":
    arr = [7, 2, 5, 3, 7, 13, 1, 6]
    arr = merge_sort(arr, 0, len(arr))
    print(arr)
