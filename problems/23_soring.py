""" Implement any sorting algorithm. """


def sort(l):
    """Sorting will modify l. """

    for i in range(len(l)-1):
        min_so_far = l[i]
        j_min = i
        for j in range(i+1, len(l)):
            if l[j] < min_so_far:
                min_so_far, j_min = l[j], j
        # Replace current element with minimum one
        l[i], l[j_min] = l[j_min], l[i]


a = [10, 3, 0, 7, 5, 100, 1, 2]
sort(a)
print(a)
