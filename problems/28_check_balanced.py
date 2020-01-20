""" Implement a funciton to check if a binary tree is balanced.
For the purposes of this question, a balanced_tree is defined
to be a tree such that the heights of the two subtrees of
any node never differ by more than one. """


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


def get_height(node, level=0):
    if node is None:
        return level
    return max(get_height(node.right, level+1), get_height(node.left, level+1))


def check_balanced(node):
    if node is None:
        return True
    height_diff = get_height(node.left) - get_height(node.right)
    if abs(height_diff) > 1:
        return False
    return check_balanced(node.left) and check_balanced(node.right)


if __name__ == "__main__":
    tree = BinaryTree(5)
    tree.insert(6)
    tree.insert(4)
    tree.insert(7)
    tree.insert(5.5)
    tree.insert(4.5)
    tree.insert(1)
    output_tree(tree.root)

    # Should output True
    print(check_balanced(tree.root))

    # Make tree unbalanced now
    tree.insert(100)
    tree.insert(101)
    tree.insert(102)
    print(check_balanced(tree.root))
