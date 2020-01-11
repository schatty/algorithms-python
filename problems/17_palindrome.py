""" Implement a function to check if a linked list is a
palindrome. """


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


def make_revsered_copy(ll):
    ll_reversed = LinkedList()
    e = ll.head
    while e is not None:
        ll_reversed.insert(e.data)
        e = e.next
    return ll_reversed


def is_palindrome(ll):
    ll_reversed = make_revsered_copy(ll)
    e1 = ll.head
    e2 = ll_reversed.head
    while e1 is not None:
        if e1.data != e2.data:
            return False
        e1 = e1.next
        e2 = e2.next
    return True


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(1)
    ll.insert(0)
    print(is_palindrome(ll))
