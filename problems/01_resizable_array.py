""" Implement ArrayList data structure and add some stuff there. """

import random


class ArrayList:
    def __init__(self, n):
        self.a = [0] * n
        self.i = 0

    def add(self, val):
        self.a[self.i] = val
        if self.i == len(self.a) - 1:
            self._increase_capacity()
        self.i += 1

    def get(self, i):
        return self.a[i]

    def _increase_capacity(self):
        cur_len = len(self.a)
        print(f"Increasing array from {cur_len} to {cur_len * 2}")
        new_a = [0] * cur_len * 2
        for i in range(len(self.a)):
            new_a[i] = self.a[i]
        self.a = new_a


if __name__ == "__main__":
    al = ArrayList(10)

    for _ in range(10_000):
        val = random.randrange(100)
        al.add(val)
