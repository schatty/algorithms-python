from math import log2 as log
from math import floor


class BinaryMinHeap(object):
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.percUp(self.current_size)

    def percDown(self, i):
        while (i * 2) <= self.current_size:
            mc = self.minChild(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i -= 1

    def clear(self):
        self.heap_list = [0]
        self.current_size = 0


class BinaryMaxHeap(object):
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.percUp(self.current_size)

    def percDown(self, i):
        while (i * 2) <= self.current_size:
            mc = self.maxChild(i)
            if self.heap_list[i] < self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def maxChild(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] > self.heap_list[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMax(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i -= 1

    def clear(self):
        self.heap_list = [0]
        self.current_size = 0


if __name__ == "__main__":
    bmax_heap = BinaryMaxHeap()

    with open('input.txt', 'r') as f:
        data = f.readlines()
    n = int(data[0])
    for op in data[1:]:
        if op.startswith("Insert"):
            val = int(op.split(" ")[-1])
            bmax_heap.insert(val)
        elif op.startswith("ExtractMax"):
            el = bmax_heap.delMax()
            print(el)
