"""
Given string, where i-th element has value of node i parent, calculate height of the tree.
Input: rooted tree with nodes {0, .., n-1}, given as sequence parent_0, ..., parent_n-1,
where parent_i - parent of the i-th node.
Output: height of the tree.
"""

# Recursive, reaches maximum recursion depth
def calc_tree_height_recursive(parent_sequence):
    tree = [[] for _ in range(len(parent_sequence))]
    for i, parent_i in enumerate(parent_sequence):
        if parent_i == -1:
            root_i = i
            continue
        tree[parent_i].append(i)

    def get_height(a, i):
        if len(a[i]) == 0:
            return 1
        max_height = 0
        for v in a[i]:
            height = get_height(a, v) + 1
            if height > max_height:
                max_height = height
        return max_height

    return get_height(tree, root_i)


# With queue
def calc_tree_height(parent_sequence):
    tree = [[] for _ in range(len(parent_sequence))]
    for i, parent_i in enumerate(parent_sequence):
        if parent_i == -1:
            root_i = i
            continue
        tree[parent_i].append(i)

    queue = [root_i]
    levels = 0
    while len(queue):
        cur_level = queue[:]
        for v in cur_level:
            queue += tree[v]
        queue = queue[len(cur_level):]
        levels += 1

    return levels



def test(foo):
    test_cases = [
        [[4, -1, 4, 1, 1], 3],
        [[-1, 0, 4, 0, 3], 4],
        [[9, 7, 5, 5, 2, 9, 9, 9, 2, -1], 4]
    ]
    for i, (input_data, expected) in enumerate(test_cases):
        res = foo(input_data)
        assert res == expected, f"Wrong case #{i+1}. Input: {input_data}. Expected {expected}, got {res}"


if __name__ == "__main__":
    test(calc_tree_height)
