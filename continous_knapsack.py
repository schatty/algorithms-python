"""
Continous knapsack problem.
First line shows number of goods in a knpackspack, foolowing
lines show pairs of cost and weight of each of the good.
Find the maximum total cost of all goods that can be placed in
a knapsack. Any good fraction can be placed inside.
"""

def main():
    n_goods, w_total = list(map(int, input().split()))
    goods = [] # list of [cost, weight] pairs
    for _ in range(n_goods):
        goods.append(list(map(int, input().split())))

    goods = sorted(goods, key=lambda x: x[0]/x[1], reverse=True)
    values = [g[0]/g[1] for g in goods]

    cost_total = 0
    for g in goods:
        if g[1] < w_total:
            w_total -= g[1]
            cost_total += g[0]
        else:
            cost_total += g[0]/g[1] * w_total
            break
    print(cost_total)


if __name__ == "__main__":
    main()
