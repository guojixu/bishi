n, m = [int(_) for _ in input().split()]

nums = []
nm = m
for _ in range(n):
    nums.append([int(_) for _ in input().split()])
    if nums[0] < 0:
        nm -= nums[0]

nums.sort(reverse=True)
dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n + 1):
    if nums[0] > 0:
        for j in range(nums[i][0], nm + 1):
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-nums[i][0]])
