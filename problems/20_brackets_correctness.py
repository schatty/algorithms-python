""" Given expression check whether brackets are in correct order. """

from collections import defaultdict

open_brackets = set(["(", "[", "{"])
close_brackers = set([")", "]", "}"])
pairs = defaultdict(lambda: "*", {"(": ")", "{": "}", "[": "]"})


class Stack:
    def __init__(self):
        self.s = []

    def push(self, data):
        self.s.append(data)

    def pop(self):
        return self.s.pop(-1)

    def __len__(self):
        return len(self.s)


def check_parenthesis(s):
    st = Stack()
    for c in s:
        if c in open_brackets:
            st.push(c)
        elif c in close_brackers:
            last_br = st.pop()
            if not pairs[last_br] == c:
                return False
    if len(st):
        return False
    return True


if __name__ == "__main__":
    s1 = "(([]))"
    print(check_parenthesis(s1))

    s2 = "([[]])[(((())))]"
    print(check_parenthesis(s2))

    s3 = "([)]"
    print(check_parenthesis(s3))

    s4 = "[[[]]]()[[())]]"
    print(check_parenthesis(s4))
