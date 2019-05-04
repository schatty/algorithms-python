"""
Check of correctness of brackets in given string.
Input: source code of some program.
Output: index of the first error or 'Success' string otherwise.
"""

class Stack(object):
    def __init__(self):
        self.l = []

    def pop(self):
        return self.l.pop()

    def push(self, v):
        self.l.append(v)

    def get(self):
        if len(self.l):
            return self.l[-1]
        return None

    def __len__(self):
        return len(self.l)


def check_brackets(str):
    stack = Stack()
    stack_index = Stack()
    for i, c in enumerate(str):
        # Put opening brackets into stack
        if c in '({[':
            stack.push(c)
            stack_index.push(i+1)
        # Check closing brackets
        brackets = ['[]', '()', '{}']
        for br_open, br_close in brackets:
            if c == br_close:
                if stack.get() != br_open:
                    return i + 1
                else:
                    stack.pop()
                    stack_index.pop()
    if len(stack) == 0:
        return 'Success'
    return stack_index.get()


def test(foo):
    test_cases = [
        ['[]', 'Success'],
        ['{}[]', 'Success'],
        ['[()]', 'Success'],
        ['(())', 'Success'],
        ['{[]}()', 'Success'],
        ['{', 1],
        ['{[}', 3],
        ['foo(bar);', 'Success'],
        ['foo(bar[i);', 10],
        ['([](){([])})', 'Success'],
        ['()[]}', 5],
        ['{{[()]]', 7],
        ['{}([]', 3]
    ]
    for i, (input_data, expected) in enumerate(test_cases):
        res = foo(input_data)
        assert res == expected, f"Wrong case #{i+1}. Input: {input_data}. Expected {expected}, got {foo(input_data)}"

if __name__ == "__main__":
    test(check_brackets)
