"Implement stack with maximum operation support."


class Stack(object):
    def __init__(self):
        self.l = []
        self.m = []

    def push(self, val):
        self.l.append(val)
        if len(self.m) == 0 or val > self.m[-1]:
            self.m.append(val)
        else:
            self.m.append(self.m[-1])

    def pop(self):
        self.m.pop()
        return self.l.pop()

    def maximum(self):
        return self.m[-1]


def stack_wrapper(commands):
    output = []
    stack = Stack()
    for com in commands:
        if com.startswith('push'):
            _, v = com.split(" ")
            v = int(v)
            stack.push(v)
        elif com.startswith('pop'):
            stack.pop()
        elif com.startswith('max'):
            output.append(stack.maximum())
    return output


def test(foo):
    test_cases = [
        [['push 1', 'push 7', 'pop'], []],
        [['push 2', 'push 1', 'max', 'pop', 'max'], [2, 2]],
        [['push 7', 'push 1', 'push 7', 'max', 'pop', 'max'], [7, 7]],
        [['push 1', 'push 2', 'max', 'pop', 'max'], [2, 1]],
        [['push 2', 'push 3', 'push 9', 'push 7', 'push 2', 'max', 'max', 'max', 'pop', 'max'], [9, 9, 9, 9]]
    ]
    for i, (input_data, expected) in enumerate(test_cases):
        res = foo(input_data)
        assert res == expected, f"Wrong case #{i+1}. Input: {input_data}. Expected {expected}, got {res}"


if __name__ == "__main__":
    test(stack_wrapper)
