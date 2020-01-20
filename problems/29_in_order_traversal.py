
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


def get_array(node, array=[]):
    if node is None:
        return array
    array = get_array(node.left) + [node.data] + get_array(node.right)
    return array


def check_binary(tree):
    tree_els_order = get_array(tree.root)
    for el1, el2 in zip(tree_els_order, sorted(tree_els_order)):
        if el1 != el2:
            return False
    return True


if __name__ == "__main__":
    tree = BinaryTree(5)
    tree.insert(6)
    tree.insert(4)
    tree.insert(7)
    tree.insert(5.5)
    tree.insert(4.5)
    tree.insert(1)
    output_tree(tree.root)

    print(check_binary(tree))

    # Now spoil the tree
    tree.root.data = 66
    print(check_binary(tree))
