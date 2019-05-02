"""
Given two strings find minimum number of edit distance between them.
"""


def calc_edit_dist(a, b):
    n, m = len(a)+1, len(b)+1
    d = [[float('inf')] * m for _ in range(n)]
    for i in range(n):
        d[i][0] = i
    for j in range(m):
        d[0][j] = j
    for i in range(1, n):
        for j in range(1, m):
            c = int(a[i-1] != b[j-1])
            d[i][j] = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+c)
    return d[-1][-1]


if __name__ == "__main__":
    a = "ab"
    b = "ab"
    print(calc_edit_dist(a, b))
