""" Write code to partition a linked list around a value x, such
that all nodes less than x come before all nodes greater
that or equal to x. If x is contained within the list, the
values of x only need to be after the elements less than x.
The partition element x can appear anywhere in the "right
partition"; it does not need toappear between the left and
right patitions. """


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


def commit_partition(ll, pivot):
    lp1 = LinkedList()
    lp2 = LinkedList()

    e = ll.head
    last_el_left = None
    while e is not None:
        if e.data < pivot:
            lp1.insert(e.data)
            if last_el_left is None:
                last_el_left = lp1.head
        else:
            lp2.insert(e.data)
        e = e.next

    # Link last element of left side to the right
    last_el_left.next = lp2.head

    return lp1


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(3)
    ll.insert(5)
    ll.insert(8)
    ll.insert(5)
    ll.insert(10)
    ll.insert(2)
    ll.insert(1)

    print("Before: \n", ll)
    ll = commit_partition(ll, 5)
    print("After:\n", ll)
