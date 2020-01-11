""" Implement an algorithm to find the kth to the last element
of a singly linked list. """

from random import randrange


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
        el = ll.head
        while el is not None:
            els.append(el.data)
            el = el.next
        return '->'.join(map(str, els))


def find_kth(ll, k):
    def find_kth(cur_node, k_target, passed=None):
        if cur_node.next is None:
            return 0, None
        k, passed_from_end = find_kth(cur_node.next, k_target, passed)
        k += 1
        if k == k_target:
            return k, cur_node
        return k, passed_from_end

    _, passed_node = find_kth(ll.head, k_target=k)
    return passed_node.data


if __name__ == "__main__":
    ll = LinkedList()
    for _ in range(10):
        ll.insert(randrange(100))
    print("Linked list: ", ll)

    print("2-th from the end: ", find_kth(ll, 2))
    print("4-th from the end: ", find_kth(ll, 4))
