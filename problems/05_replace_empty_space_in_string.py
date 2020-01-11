""""Write a method to replace all spaces in a string with '%20'.
You may assume that the string has suffcient space at the end to
hold the additional characters, and that you are given the true
length of the string. Use a character array so that you can perform
this operation in place. """


def fill_spaces(s, n, fill_with="%20"):
    space_count = s1.count(" ")
    s = s + " " * space_count * 3
    s = bytearray(s, "utf-8")
    offset = space_count * 3
    i_orig = n
    i_offset = n + offset
    while i_orig > 0:
        if s[i_orig] != ord(" "):
            s[i_offset] = s[i_orig]
            i_offset -= 1
        else:
            s[i_offset] = ord("0")
            s[i_offset-1] = ord("2")
            s[i_offset-2] = ord("%")
            i_offset -= 3
        i_orig -= 1
    return s[-n-offset-1:].decode()


s1 = "Mr John Smith "
n = 13
print(fill_spaces(s1, n))
