""" Given a binary tree, design an algorithm which creates a linked list
of all nodes at each level (e.g. if you have a tree with depth D, you'll
have D linked list. """


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


class NodeTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, data):
        self.root = NodeTree(data)

    def insert(self, data):
        cur_node = self.root
        while cur_node is not None:
            if data > cur_node.data:
                if cur_node.right is None:
                    cur_node.right = NodeTree(data)
                    break
                else:
                    cur_node = cur_node.right
            else:
                if cur_node.left is None:
                    cur_node.left = NodeTree(data)
                    break
                else:
                    cur_node = cur_node.left


def output_tree(tree, level=" "):
    l_el = "-" if tree.left is None else tree.left.data
    r_el = "-" if tree.right is None else tree.right.data
    print(f"{level} {tree.data} ({l_el} {r_el})")
    if tree.left is not None:
        output_tree(tree.left, level=level*2)
    if tree.right is not None:
        output_tree(tree.right, level=level*2)


def traverse_tree(node, level, lls):
    if node is None:
        return
    lls[level].insert(node.data)
    traverse_tree(node.left, level+1, lls)
    traverse_tree(node.right, level+1, lls)


def gather_linked_lists_by_level(tree):
    lls = [LinkedList() for _ in range(3)]
    traverse_tree(tree.root, level=0, lls=lls)
    return lls


if __name__ == "__main__":
    tree = BinaryTree(5)
    tree.insert(6)
    tree.insert(4)
    tree.insert(7)
    tree.insert(5.5)
    tree.insert(4.5)
    tree.insert(1)
    output_tree(tree.root)

    lls = gather_linked_lists_by_level(tree)
    print("LINKED LISTS: ")
    for i, ll in enumerate(lls):
        print(f"Level {i}: {ll} ")
