"""Implement an algorithm to delete a node in the middle (i.e., any
node but the first and last node, not necessary the exact middle of
a singly linked list, given only access to that node. """

import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def __str__(self):
        els = []
        el = self.head
        while el is not None:
            els.append(el.data)
            el = el.next

        return "->".join(map(str, els))


def get_kth_node(ll, k):
    n = ll.head
    for i in range(k):
        n = n.next
    return n


def delete_node(ll, node):
    data = node.next.data
    node.data = data
    node.next = node.next.next


if __name__ == "__main__":
    ll = LinkedList()
    for _ in range(10):
        ll.insert(random.randrange(100))

    print("Original: ", ll)
    node = get_kth_node(ll, 4)
    delete_node(ll, node)
    print("With deleted 5-th: ", ll)
