""" Given a circular linked list, implement an algorithm
that returns the node at the beginning of the loop. """


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

    def create(self, l):
        for data in l:
            self.insert(data)

    def get_nth(self, n):
        e = self.head
        for _ in range(n):
            e = e.next
        return e

    def __str__(self):
        c = 0
        els = []
        e = self.head
        while e is not None and c < 20:
            els.append(e.data)
            c += 1
            e = e.next

        s = "->".join(map(str, els))
        if c == 20:
            s += "..."
        return s


def find_loop(ll):
    slow = ll.head
    fast = ll.head.next

    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    return slow


if __name__ == "__main__":
    ll = LinkedList()
    ll.create(["E", "D", "C", "B", "A"])
    looped = ll.get_nth(2)
    last = ll.get_nth(4)
    last.next = looped

    print("Looped element: ", find_loop(ll).data)
