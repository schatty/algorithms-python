"""
First row contains numbers 1 <= W <= 10e4 and 1 <= n <= 300 that shows knapsack
weight limit and number of golden bars. Items contain n weights of golden bars.
Find maximum weight that one can bring in the knapsack.
"""

def calc_max_value(W, items):
    d = [[0] * (len(items)+1) for _ in range(W+1)]
    for w in range(W+1):
        d[w][0] = 0
    for i in range(len(items)+1):
        d[0][i] = 0
    for i in range(1, len(items)+1):
        for w in range(1, W+1):
            d[w][i] = d[w][i-1]
            if items[i-1] <= w:
                d[w][i] = max(d[w][i], d[w-items[i-1]][i-1]+items[i-1])
    return d[-1][-1]


if __name__ == "__main__":
    W = 10
    items = [1, 4, 8]
    print(calc_max_value(W, items))
