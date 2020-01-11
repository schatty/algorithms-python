"""Given an image repsresented by an NxN matrix, write
a method to rotate the image by 90 degrees. """


a = [[1, 2, 3, 4, 5],
     [1, 2, 3, 4, 5],
     [1, 2, 3, 4, 5],
     [1, 2, 3, 4, 5],
     [1, 2, 3, 4, 5]]


def rotate(a):
    n = len(a)
    for layer in range(0, n//2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first

            # Save top to buffer
            top  = a[first][i]

            # left -> top
            a[first][i] = a[last-offset][first]

            # bottom -> left
            a[last-offset][first] = a[last][last-offset]

            # right -> bottom
            a[last][last-offset] = a[i][last]

            # top -> right
            a[i][last] = top

    return a


print(rotate(a))
