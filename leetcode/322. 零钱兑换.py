

coins = [int(_) for _ in input().split(',')]

amount = int(input())


dp = [float('inf')] * (amount + 1)

dp[0] = 0

for coin in coins:
    for x in range(coin, amount + 1):
        dp[x] = min(dp[x], dp[x-coin] + 1)


print(dp[-1])