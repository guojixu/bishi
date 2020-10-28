
def paycoins():

    coins = [int(_) for _ in input().split(',')]

    amount = int(input())


    dp = [float('inf')] * (amount + 1)

    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x-coin] + 1)

    print(dp[-1])

    dp = [float('inf')] * (amount + 1)

    dp[0] = 0

    for coin in coins:
        for x in range(amount + 1, coin):
            dp[x] = min(dp[x], dp[x-coin] + 1)

    print(dp[-1])
    #

# 体积不少于v，价值最小


'''
3 6
2 5
3 4
4 3

7
v, w 选择第2和第3个物品。


6 10
2 4
3 4
4 5
5 11
6 10
7 11

15
选择第3和第5个物品，或者第2和第6个物品。

'''


def my_package():

    n, V = [int(_) for _ in input().split()]

    com = []

    max_value = 0

    for _ in range(n):
        curr = [int(_) for _ in input().split()]
        max_value += curr[1]
        com.append(curr)

    dp = [0] * (max_value + 1)

    for i in range(0, n):

        for j in range(max_value, com[i][1]-1, -1):

            dp[j] = max(dp[j], dp[j-com[i][1]] + com[i][0])

    for i in range(1, max_value):

        if dp[i] >= V:
            print(i)
            exit(0)

my_package()














































