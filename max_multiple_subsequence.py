"""
Given array find maximum k that there is exists subsequence of size k in which
every following element is multiple of the previous one. 
"""

def get_max_subseq(a):
    d = [0] * len(a)
    for i in range(len(a)):
        d[i] = 1
        for j in range(i):
            if a[i] % a[j] == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    return max(d)

if __name__ == "__main__":
    a = [3, 6, 7, 12]
    suba = get_max_subseq(a)
    print(suba)
