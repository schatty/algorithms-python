"""
Given sting and pattern find all occurences (index of start) of pattern in a string.
"""

if __name__ == "__main__":

    def calc_hash(s):
        h = 0
        p = 1_000_000_007
        x = 1
        for i in range(len(s)):
            h += (ord(s[i])%p) * ((x**i) % p)
        return h

    pattern = "aba"
    st = "abacaba"

    #pattern = "Test"
    #st = "testTesttesT"

    #pattern = "aaaaa"
    #st = "baaaaaaa"

    #pattern = "aaa"
    #st = "aaaaaaab"

    inds = []
    m = len(pattern)
    pattern_hash = calc_hash(pattern)
    st_hash = calc_hash(st[-m:])
    # First comparison with first hash
    if pattern_hash == st_hash:
        if pattern == st[-m:]:
            inds.append(len(st)-m)


    p = 1_000_000_007
    x = 1
    for i in range(len(st)-1,  m-1, -1):
        st_hash = (( st_hash - ord(st[i]) * x**(m-1) ) * x + ord(st[i-m])) % p
        if pattern_hash == st_hash:
            if pattern == st[i-m:i]:
                inds.append(i-m)
    inds = reversed(inds)

    print(" ".join(map(str, inds)))
