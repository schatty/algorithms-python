""" Implement a method to perform basic string compressing using
the counts of repeated characters. For example, the string
aabccccaaa would become a2b1c5a3. If the compressed string would
not become smaller that the original string, your method should
return the original string. You can assume the string has only
uppercase and lowercase """


def compress(s):
    s_compressed = ""
    c = 1
    cur_sym = s[0]
    for i in range(1, len(s)):
        if s[i] != cur_sym:
            s_compressed += f"{cur_sym}{c}"
            cur_sym = s[i]
            c = 1
        else:
            c += 1

    # Last symbol
    s_compressed += f"{cur_sym}{c}"
    return s_compressed


s = "aabccccaaa"
print(compress(s))
