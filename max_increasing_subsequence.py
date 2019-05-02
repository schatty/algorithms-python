"""
Given array find maximum subsequence of increasing elements.
"""

def get_max_subseq(a):
    d = [0] * len(a)
    for i in range(len(a)):
        d[i] = 1
        for j in range(i):
            if a[j] < a[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1

    # Length of maximum subsequence
    ans = max(d)

    # Subsequence reconstruction
    k = d.index(ans)
    subs = [a[k]]
    k_prev = k
    k -= 1
    while k > 0:
        if d[k]  == d[k_prev] - 1 and a[k] < subs[0]:
             subs = [a[k]] + subs
             k_prev = k
        k -= 1
    return subs

if __name__ == "__main__":
    a = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]
    suba = get_max_subseq(a)
    print(suba)
