def selection_sort(a):
    for i in range(len(a)):
        k = i
        for j in range(i+1, len(a)):
            if a[j] < a[k]:
                k = j
        tmp = a[i]
        a[i] = a[k]
        a[k] = tmp
    return a


if __name__ == "__main__":
    arr = [10, 7, 0, 1, 8, 2]
    arr = selection_sort(arr)
    print(arr)
