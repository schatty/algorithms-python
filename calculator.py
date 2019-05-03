"""
Given a privimite calculator that can only perform actions: x+1, 2*x, 3*x calculate
minimum number of actions to achieve given number from 1 and print that actions.
"""

def get_min_num_operations(n):
    d = [float("inf")] * (n+1)
    d[1] = 0
    for i in range(1, n):
        if i + 1 <= n:
            if d[i+1] > d[i] + 1:
                d[i+1] = d[i]+1
        if i*2 <= n:
            if d[i*2] > d[i]+1:
                d[i*2] = d[i] + 1
        if i*3 <= n:
            if d[i*3] > d[i]+1:
                d[i*3] = d[i] + 1

    # Reconstrution of the actions
    k = n
    actions = [k]
    while k > 1:
        for i in range(1, k, 1):
            if d[i] == d[k] - 1:
                if i*2 == k:
                    actions = [i] + actions
                    k //= 2
                    break
                if i*3 == k:
                    actions = [i] + actions
                    k //= 3
                    break
                if i+1 == k:
                    actions = [i] + actions
                    k -= 1
                    break
    return d[n], actions

if __name__ == "__main__":
    n = 5
    n_actions, actions = get_min_num_operations(n)
    print(n_actions, actions)
