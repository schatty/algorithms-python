"""Assume you have a method isSubstring which checks
if one word is a substring of another. Given two strings,
s1 and s2, write code to check if s2 is a rotation of
s1 using only one call to isSubstring (e.g. "waterbottle"
is a rotation of "erbottlewat") """


def is_substring(s1, s2):
    return s2 in s1


def is_rotation(s1, s2):
    if len(s1) == len(s2):
        if s2 in s1 + s1:
            return True
    return False


s1 = "waterbottle"
s2 = "erbottlewat"
print(is_rotation(s1, s2))


s1 = "waterbottle"
s2 = "erbottlewae"
print(is_rotation(s1, s2))
