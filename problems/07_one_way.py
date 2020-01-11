"""There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character. Given
two string, write a function to check if they are one edit (or zero edits)
away. """


def is_replacement(s1, s2):
    seen_repl = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if not seen_repl:
                seen_repl = True
            else:
                return False
    return True


def is_insertion(s1, s2):
    """ s1 < s2 """
    seen_insert = False
    i1 = 0
    i2 = 0
    while i1 != len(s1) - 1:
        if s1[i1] != s2[i2]:
            if not seen_insert:
                seen_insert = True
                i2 += 1
            else:
                return False
        else:
            i1 += 1
            i2 += 1
    return True


def one_away(s1, s2):
    if len(s1) == len(s2):
        return is_replacement(s1, s2)
    elif len(s1) < len(s2):
        return is_insertion(s1, s2)
    else:
        return is_insertion(s2, s1)


print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))

