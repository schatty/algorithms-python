"""
Given string find most frequent substring of size k.
"""

def calc_hash(s, x=263, p=1_000_000_007):
    h = 0
    for i in range(len(s)):
        h += (ord(s[i])%p) * ((x**i) % p)
    return h

if __name__ == "__main__":
    m = 3
    st = "abacabadskdfabacabkjdjfkdjabacabowfabacabaabacablasdfabacab"

    x = 263
    p = 100_000
    st_hash = calc_hash(st[-m:], x=x, p=p)

    encounters = [[] for _ in range(p)]
    max_index = 0
    max_hash = None

    for i in range(len(st)-1,  m-1, -1):
        st_hash = (( st_hash - ord(st[i]) * x**(m-1) ) * x + ord(st[i-m])) % p
        encounters[st_hash].append(i)
        if len(encounters[st_hash]) > max_index:
            max_index = i
            max_hash = st_hash

    print("Most frequent substring: ", st[max_index-m+1:max_index+1], len(encounters[max_hash]))

    lens = 0
    unique_subs = 0
    for enc in encounters:
        if len(enc):
            unique_subs += 1
            lens += len(enc)
    print("Mean of repeating substrings: ", lens / unique_subs)
