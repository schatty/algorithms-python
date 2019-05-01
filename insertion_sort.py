def insertion_sort(a):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j-1]:
            tmp = a[j]
            a[j] = a[j-1]
            a[j-1] = tmp
            j -= 1
    return a


if __name__ == "__main__":
    arr = [10, 7, 0, 1, 8, 2]
    arr = insertion_sort(arr)
    print(arr)
