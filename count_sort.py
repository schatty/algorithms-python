"""
We have an assumption that intitial array contains positive number from 1..N
"""

def count_sort(a, m):
    b = [0] * m
    a_sorted = [0] * len(a)
    # Count elmenets in b
    for j in range(len(a)):
        b[a[j]-1] += 1
    # Cumulative sums
    for i in range(1, m):
        b[i] += b[i-1]
    # Fill empty array based on cumulative sums
    for j in range(len(a)-1, -1, -1):
        a_sorted[b[a[j]-1]-1] = a[j]
        b[a[j]-1] -= 1
    return a_sorted


if __name__ == "__main__":
    arr = [2, 1, 1, 1, 3, 2, 2, 2, 3, 2, 3, 2, 2, 1, 1]
    print(count_sort(arr, 3))
