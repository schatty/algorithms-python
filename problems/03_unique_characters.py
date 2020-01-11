"""Implement an algorithm to determine if a string has all unique characters. """


def check_unique(s):
    hash_table = {}
    for c in s:
        if c in hash_table:
            return False
        hash_table[c] = True
    return True


s1 = "UNIQE"
s2 = "All unique"
s3 = "asdfghjkl;qwertyuiop"

print(check_unique(s1))
print(check_unique(s2))
print(check_unique(s3))
