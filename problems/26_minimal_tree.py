""" Given a sorted (increasing order) array with unique integer
elements, write an algorithm to create a binary search tree
with minimal hight. """


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.l = None
        self.r = None


def create_minimal_bt(a, start, end):
    if end < start:
        return None
    mid = (start + end) // 2
    node = TreeNode(a[mid])
    node.l = create_minimal_bt(a, start, mid-1)
    node.r = create_minimal_bt(a, mid+1, end)
    return node


def output_tree(tree, level=" "):
    l_el = "-" if tree.l is None else tree.l.data
    r_el = "-" if tree.r is None else tree.r.data
    print(f"{level} {tree.data} ({l_el} {r_el})")
    if tree.l is not None:
        output_tree(tree.l, level=level*2)
    if tree.r is not None:
        output_tree(tree.r, level=level*2)


if __name__ == "__main__":
    print("4 elment tree: ")
    a = [1, 2, 3, 4]
    tree = create_minimal_bt(a, 0, len(a)-1)
    output_tree(tree)

    print("5 element tree: ")
    a = [1, 2, 3, 4, 5]
    tree = create_minimal_bt(a, 0, len(a) - 1)
    output_tree(tree)
