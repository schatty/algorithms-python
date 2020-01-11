"Given two strings, write a method to decide if one is a permutation fo the other. """

def is_permutation(s1, s2):
    d = {}
    for c in s1:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    for c in s2:
        if c not in d:
            return False
        else:
            d[c] = d[c] - 1
    for k in d:
        if d[k] != 0:
            return False
    return True


s1 = "catseetonashelf"
s2 = "shelfseetonacat"
print(is_permutation(s1, s2))

s1 = "catdog"
s2 = "hotdog"
print(is_permutation(s1, s2))
