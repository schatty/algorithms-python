"""
Rearrange given array so that resulting array will be a heap.
Input: Array A[0, ..., n-1]
Output: printed rearrangement of pairs of the elements (one at a row)
"""

from math import floor

H = [0]
size = 0
n_swaps = 0

def parent(i):
    return floor(i/2)


def left_child(i):
    return 2 * i


def right_child(i):
    return 2 * i + 1


def sift_up(i):
    while i > 1 and H[parent(i)] < H[i]:
        tmp = H[parent(i)]
        H[parent(i)] = H[i]
        H[i]= tmp
        i = parent(i)


def sift_down(i):
    global H
    global n_swaps

    outputs = []
    max_index = i
    l = left_child(i)
    if l <= size and H[l] < H[max_index]:
        max_index = l
    r = right_child(i)
    if r <= size and H[r] < H[max_index]:
        max_index = r
    if i != max_index:
        outputs.append([i-1, max_index-1])
        n_swaps += 1
        tmp = H[i]
        H[i] = H[max_index]
        H[max_index] = tmp
        outputs += sift_down(max_index)
    return outputs

def insert(p):
    if size == max_size:
        H += [0] * len(H)
        max_size = len(H)
    size += 1
    H[size] = p
    sift_up(size)

def extract_max():
    result = H[1]
    H[1] = H[size]
    size -= 1
    sift_down(1)
    return result

def remove(i):
    H[i] = float("inf")
    sift_up(i)
    extract_max()


def change_priority(i, p):
    old_p = H[i]
    H[i] = p
    if p < old_p:
        sift_up(i)
    else:
        sift_down(i)


def build_heap(a):
    global H
    global size
    global n_swaps

    H = [0] + a
    size = len(a)
    n_swaps = 0
    swaps = []
    for i in range(floor(size/2), 0, -1):
        swaps += sift_down(i)

    print("n_swaps: ", n_swaps)
    print("swaps: ", swaps)


if __name__ == "__main__":
    build_heap([7, 6, 5, 4, 3, 2])
