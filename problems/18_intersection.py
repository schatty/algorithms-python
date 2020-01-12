""" Given two (singly) linked lists, determine if the two lists
intersect. Return the intersecting node. """


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

    def get_nth(self, n):
        el = self.head
        for _ in range(n):
            el = el.next
        return el

    def __len__(self):
        ll_len = 1
        e = self.head
        while e is not None:
            ll_len += 1
            e = e.next
        return ll_len


def reverse_inplace(ll):
    prev_node = None
    cur_node = ll.head
    next_node = cur_node.next
    while cur_node is not None:
        next_node = cur_node.next
        cur_node.next = prev_node
        # Step
        prev_node = cur_node
        cur_node = next_node

    ll.head = prev_node


def find_insertecting_node(ll1, ll2):
    l1 = len(ll1)
    l2 = len(ll2)
    if l1 >= l2:
        e1 = ll1.get_nth(l1 - l2)
        e2 = ll2.head
    else:
        e2 = ll2.get_nth(l2 - l1)
        e1 = e1.head

    while e1.data != e2.data:
        e1 = e1.next
        e2 = e2.next
    return e1


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.insert(1)
    ll1.insert(2)
    ll1.insert(7)
    ll1.insert(9)
    ll1.insert(5)
    ll1.insert(1)
    ll1.insert(3)

    i_node = ll1.get_nth(4)
    print("True intersecting node: ", i_node.data)

    # Link second list
    ll2 = LinkedList()
    ll2.insert(6)
    ll2.insert(4)
    last_node = ll2.get_nth(1)
    last_node.next = i_node

    print("LL1: ", ll1)
    print("LL2: ", ll2)

    print("Foun intersecting node: ", find_insertecting_node(ll1, ll2).data)
