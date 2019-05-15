"""
Given number of nodes n and nodes in format
key_i, left_i, right_i print out three different version of walking of tree:
1. in-order
2. pre-order
3. post-order
"""


class Node(object):
    def __init__(self, index, k=None):
        self.i = index
        self.k = k
        self.l = None
        self.r = None

    def __str__(self):
        return str(self.k)

def in_order(node):
    if node is None or node.i == -1:
        return []
    l = []
    l += in_order(node.l)
    l += [str(node)]
    l += in_order(node.r)
    return l


def pre_order(node):
    if node is None or node.i == -1:
        return []
    l = [str(node)]
    l += pre_order(node.l)
    l += pre_order(node.r)
    return l


def post_order(node):
    if node is None or node.i == -1:
        return []
    l = []
    l += post_order(node.l)
    l += post_order(node.r)
    return l + [str(node)]


if __name__ == "__main__":
    n = 5
    nodes = [
        [4, 1, 2],
        [2, 3, 4],
        [5, -1, -1],
        [1, -1, -1],
        [3, -1, -1]
    ]

    '''
    n = 10
    nodes = [
        [0, 7, 2],
        [10, -1, -1],
        [20, -1, 6],
        [30, 8, 9],
        [40, 3, -1],
        [50, -1, -1],
        [60, 1, -1],
        [70, 5, 4],
        [80, -1, -1],
        [90, -1, -1]
    ]
    '''

    tree = [Node(i) for i in range(n)]
    for i, node in enumerate(nodes):
        tree[i].k = node[0]
        if node[1] > -1:
            tree[i].l = tree[node[1]]
        if node[2] > -1:
            tree[i].r = tree[node[2]]

    print(" ".join(in_order(tree[0])))
    print(" ".join(pre_order(tree[0])))
    print(" ".join(post_order(tree[0])))
