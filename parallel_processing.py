"""
Given n processors and m tasks calculate time of the processing start and number
of processor for that task.

Input: number of processes n and sequence of of numbers t_0..t_m-1 where
t_i - time to process i-th task
Output: time of start processing and number of corresponding processor for each of the tasks
if there are multiple free processors, tasks is given to one with minimal number.
"""

from math import floor


class MinHeap(object):
    def __init__(self):
        self.H = [None] + [None] * int(1e5)
        self.size = 0
        self.max_size = len(self.H)-1

    def sift_up(self, i):
        ip = i//2
        while i > 1 and self.H[ip][0] > self.H[i][0]:
            self.H[i], self.H[ip] = self.H[ip], self.H[i]
            i = ip
            ip = i//2

    def sift_down(self, i):
        max_index = i
        l = i*2
        if l <= self.size and self.H[l][0] <= self.H[max_index][0]:
            if self.H[l][0] == self.H[max_index][0]:
                if self.H[l][1] < self.H[max_index][1]:
                    max_index = l
            else:
                max_index = l
        r = i*2+1
        if r <= self.size and self.H[r][0] <= self.H[max_index][0]:
            if self.H[r][0] == self.H[max_index][0]:
                if self.H[r][1] < self.H[max_index][1]:
                    max_index = r
            else:
                max_index = r

        if i != max_index:
            self.H[i], self.H[max_index] = self.H[max_index], self.H[i]
            self.sift_down(max_index)

    def insert(self, p):
        if self.size+1 == self.max_size:
            self.H += [None] * len(self.H)
            self.max_size = len(self.H)
        self.size += 1
        self.H[self.size] = p
        self.sift_up(self.size)

    def extract_min(self):
        if self.size == 0:
            return None

        result = self.H[1]
        self.H[1] = self.H[self.size]
        self.size -= 1
        self.sift_down(1)

        return result


def run_sim(m, tt):
    h = MinHeap()
    for i in range(m):
        h.insert([0, i])

    for t in tt:
        el = h.extract_min()
        print(el[1], el[0])
        h.insert([el[0]+t, el[1]])

if __name__ == "__main__":
    run_sim(m=4, tt=[1]*20)
