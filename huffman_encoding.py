"""
Convert given string into optimal binary code via
Huffman coding. 
In the first line output number of unique symbol in a string 
and total length of the encoded string, on the following 
lines output symbols with corresponding codes.
"""

class OrderQueue(object):
    def __init__(self, l):
        self.l = l

    def extract_min(self):
        k = min(self.l, key=lambda x: x['value'])
        self.l.remove(k)
        return k

    def add(self, node):
        self.l.append(node)

    def __len__(self):
        return len(self.l)


class Tree(object):
    def __init__(self, struct):
        self.struct = struct

    def get_node_codes(self):
        def get_node_code(node, prefix=''):
            if node['sym'] is not None:
                return {node['sym']: prefix}
            d = {}
            if node['l'] is not None:
                d = {**d, **get_node_code(node['l'], prefix+'0')}
            if node['r'] is not None:
                d = {**d, **get_node_code(node['r'], prefix+'1')}
            return d
        # Edge case with tree contains only one node
        if self.struct['l'] is None and self.struct['r'] is None:
            return {self.struct['sym']: '0'}
        return get_node_code(self.struct)
        

def main():
    string = input()
    init_codes = []
    for s in string:
        for el in init_codes:
            if el['sym'] == s:
                el['value'] += 1
                break
        else:
            init_codes.append({'sym': s, 'value': 1, 'l': None, 'r': None})

    ordered_queue = OrderQueue(init_codes)
    
    while len(ordered_queue) > 1:
        l = ordered_queue.extract_min()
        r = ordered_queue.extract_min()
        new_node = {'sym': None, 'value': l['value'] + r['value'], 'l': l, 'r': r}
        ordered_queue.add(new_node)
    tree = Tree(ordered_queue.l[0])  
    huffman_codes = tree.get_node_codes()
    encoded_string = ''.join([huffman_codes[c] for c in string])
    print(len(huffman_codes), len(encoded_string))
    for c in sorted(huffman_codes, key=lambda x: len(huffman_codes[x])):
        print(c, ': ', huffman_codes[c])
    print(encoded_string)

if __name__ == "__main__":
    main()
