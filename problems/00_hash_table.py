"""Implement data structure of hash-table and insert some stuff there. """

import uuid
import string
import random


class Node:
    def __init__(self, val, p_next=None):
        self.val = val
        self.next = p_next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
        
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next

        cur_node.next = Node(val)

    def get(self, key):
        cur_node = self.head
        while True:
            if cur_node.val[0] == key:
                return cur_node.val
            if cur_node.next is None:
                break
            cur_node = cur_node.next
        return None


class HashTable:
    def __init__(self, n=1000):
        self.a = [LinkedList() for _ in range(1000)]

    def compute_hash(self, obj):
        return hash(obj) % 1499

    def add(self, key, val):
        i = self.compute_hash(key) % len(self.a)
        self.a[i].append((key, val))
        
    def get(self, key):
        i = self.compute_hash(key) % len(self.a)
        val = self.a[i].get(key)
        return val


def random_string():
    letters = string.ascii_lowercase
    return ''.join([random.choice(letters) for _ in range(10)])


if __name__ == "__main__":
    hash_table = HashTable()

    keys = [random_string() for _ in range(10000)]
    vals = [random.randrange(1000) for _ in range(10000)]
    elements = [(k, v) for k, v in zip(keys, vals)]
    
    for e in elements:
        hash_table.add(e[0], e[1])
    print("Elements added successfully!")

    print(f"Getring element {elements[14]}: ")
    print(hash_table.get(elements[14][0]))
