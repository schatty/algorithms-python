"""
Given natural number 1 <= n <= 10^9 find maximal number k
for which n can be presented as a sum of k unique numbers.
Output k in the first line, the numbers on the second.
"""

def main():
    n = int(input())

    # Edge case n = 1
    if n == 1:
        print("1\n1")
        return 

    cur_n = 1
    nums = []
    while n:
        if n - cur_n <= cur_n:
            nums.append(n)
            break
        else:
            n -= cur_n
            nums.append(cur_n)
            cur_n += 1

    print(len(nums))
    print(' '.join(map(str, nums)))


if __name__ == "__main__":
    main()
