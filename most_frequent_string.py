"""
Given string find most frequent substring of size k.
"""

def calc_hash(s, x=263, p=1_000_000_007):
    h = 0
    for i in range(len(s)):
        h += ((ord(s[i])%p) * ((x**i) % p))
    return h % p

if __name__ == "__main__":
    m = 6
    st = "abacabadskdfabacabkjdjfkdjabacabowfabacabaabacablasdfabacab"

    x = 263
    p = 100_000
    st_hash = calc_hash(st[-m:], x=x, p=p)

    encounters = [[] for _ in range(p)]
    print(st_hash)
    encounters[st_hash].append(len(st)-m)
    max_index = len(st)-m
    max_hash = st_hash

    for i in range(len(st)-1,  m-1, -1):
        st_hash = (( st_hash - ord(st[i]) * x**(m-1) ) * x + ord(st[i-m])) % p
        encounters[st_hash].append(i-m)
        if len(encounters[st_hash]) > max_index:
            max_index = i-m
            max_hash = st_hash

    print("Most frequent substring: ", st[max_index:max_index+m], len(encounters[max_hash]))

    lens = 0
    unique_subs = 0
    for enc in encounters:
        if len(enc):
            unique_subs += 1
            lens += len(enc)
    print("Mean of repeating substrings: ", lens / unique_subs)
