"""
The first row contains number of elements in the array as a first number and
elements as following.
The second row contains elements we want to find. Output indices of the elements.
"""
from math import floor


def find_binary(arr, el):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = floor((l+r)/2)
        if arr[m] == el:
            return m + 1 # +1 for to start from 1
        elif arr[m] > el:
            r = m - 1
        else:
            l = m + 1
    return -1


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = list(map(int, f.readline().split(" ")))
        n, arr = data[0], data[1:]
        elements_to_find = list(map(int, f.readline().split(" ")))
        elements_to_find = elements_to_find[1:]

    inds = []
    for el in elements_to_find:
        inds.append(find_binary(arr, el))
    print(" ".join(map(str, inds)))
