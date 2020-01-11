""" Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0. """


def output_matrix(a):
    for l in a:
        print(" ".join(map(str, l)))

def fill_zeros(a):
    # First pass (indices saving)
    i_rows = [False for _ in range(len(a))]
    j_cols = [False for _ in range(len(a[0]))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 0:
                i_rows[i] = True
                j_cols[j] = True

    # Second pass (zero fill)
    for i_zero in range(len(i_rows)):
        if i_rows[i_zero]:
            for j in range(len(a[0])):
                a[i_zero][j] = 0
    for j_zero in range(len(j_cols)):
        if j_cols[j_zero]:
            for i in range(len(a)):
                a[i][j_zero] = 0

    return a


a = [[1, 2, 3, 5, 0],
     [1, 1, 0, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1]]
output_matrix(fill_zeros(a))

