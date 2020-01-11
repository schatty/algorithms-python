""" Implement StringBuilder, a class that concatenates strings via
ArrayList structure. """

import random
import string


class ArrayList:
    def __init__(self, n):
        self.a = [0] * n
        self.i = 0

    def add(self, s):
        if self.i + len(s) >= len(self.a):
            self._increase_capacity()

        for c in s:
            self.a[self.i] = c
            self.i += 1

    def get_string(self):
        return ''.join(self.a[:self.i])

    def _increase_capacity(self):
        cur_len = len(self.a)
        print(f"Increasing array from {cur_len} to {cur_len * 2}")
        new_a = [0] * cur_len * 2
        for i in range(len(self.a)):
            new_a[i] = self.a[i]
        self.a = new_a


class StringBuilder:
    def __init__(self):
        self.la = ArrayList(10)

    def concat(self, new_string):
        self.la.add(new_string)

    def get(self):
        return self.la.get_string()


def get_random_string():
    letters = string.ascii_lowercase
    return ''.join([random.choice(letters) for _ in range(10)])


if __name__ == "__main__":
    sb = StringBuilder()

    for _ in range(20):
        s = get_random_string()
        sb.concat(s)

    print("Resulting string: ", sb.get())
