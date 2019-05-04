"""
Given a sequence of size n and a window size m find n-m+1 maximums in sliding window
in O(n) operations.
"""

class QueueMax(object):
    def __init__(self):
        self.l = []

    def get_max(self):
        return self.l[0]

    def add(self, val):
        while len(self.l) and self.l[-1] < val:
            self.l.pop()
        self.l.append(val)

    def pop(self, val):
        if self.l[0] == val:
            self.l.pop(0)

def get_maximum_slides(vals, m):

    if m == 1:
        return vals

    outputs = []
    queue = QueueMax()
    for i in range(m-1):
        queue.add(vals[i])
    outputs = []
    for i in range(m-1, len(vals)):
        queue.add(vals[i])
        outputs.append(queue.get_max())
        queue.pop(vals[i-m+1])
    return outputs

def test(foo):
    test_cases = [
        [([2, 7, 3, 1, 5, 2, 6, 2], 4), [7, 7, 5, 6, 6]],
        [([2, 1, 5], 1), [2, 1, 5]],
        [([2, 3, 9], 3), [9]],
        [([2, 7, 3, 1, 5, 2, 6, 2], 4), [7, 7, 5, 6, 6]],
        [([16, 79, 20, 19, 43, 72, 78, 33, 40, 52, 70, 79, 66, 43, 60], 12), [79, 79, 79, 79]],
        [([73, 65, 24, 14, 44, 20, 65, 97, 27, 6, 42, 1, 6, 41, 16], 7), [73, 97, 97, 97, 97, 97, 97, 97, 42]],
    ]
    for i, (input_data, expected) in enumerate(test_cases):
        res = foo(*input_data)
        assert res == expected, f"Wrong case #{i+1}. Input: {input_data}. Expected {expected}, got {res}"


if __name__ == "__main__":
    test(get_maximum_slides)
