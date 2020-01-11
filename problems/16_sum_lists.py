""" You have two numbers represented by a linked list, where
each node contains a single digit. The digits are stored in
reverse order, such that that 1's digit is at the head of the
list. Write a function that adds the two numbers and returns
the sum as a linked list. """


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
        return "".join(map(str, els))


def sum_lists(l1, l2):
    carry = 0
    e1 = l1.head
    e2 = l2.head
    l3 = LinkedList()
    while e1 is not None and e2 is not None:
        n1 = int(e1.data)
        n2 = int(e2.data)

        n = carry + n1 + n2
        l3.insert(n % 10)
        carry = n // 10

        e1 = e1.next
        e2 = e2.next

    if e1 is None:
        while e2 is not None:
            n = e2.data + carry
            l3.insert(n)
            if carry != 0:
                carry = 0
            e2 = e2.next
    else:
        while e1 is not None:
            n = e1.data + carry
            l3.insert(n)
            if carry != 0:
                carry = 0
            e1 = e1.next
    return l3


if __name__ == "__main__":
    l1 = LinkedList()
    l1.insert(6)
    l1.insert(1)
    l1.insert(7)

    l2 = LinkedList()
    l2.insert(2)
    l2.insert(9)
    l2.insert(5)

    l3 = sum_lists(l1, l2)
    print(f"Sum of {l1} and {l2} is {l3}")
