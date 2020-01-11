"""Write code to remove duplicates from an unsorted linked list. """

import random
from collections import defaultdict


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
        
    def __str__(self):
        els = []
        e = self.head
        while e is not None:
            els.append(e.val)
            e = e.next
        return '->'.join(map(str, els))


def remove_duplicates(ll):
    e = ll.head
    seen = set()
    prev = None

    while e is not None:
        if e.val in seen:
            if e.next is not None:
                prev.next = e.next
        else:
            seen.add(e.val)
            prev = e
        e = e.next

    return ll


if __name__ == "__main__":
    ll = LinkedList()
    for _ in range(30):
        ll.append(random.randrange(10))
    print(ll)

    ll = remove_duplicates(ll)
    print(ll)
