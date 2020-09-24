n = int(input())

dp = [0] * (n + 1)

dp[1] = 1

for i in range(1, n + 1):
    for j in range(i):

        if 2 ** j <= i:
            dp[i] += dp[i - 2 ** j]

print(dp[-1])