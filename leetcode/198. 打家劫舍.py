

nums = [int(_) for _ in input().split(',')]

dp = [0] * len(nums)

dp[0] = nums[0]

dp[1] = max(nums[0], nums[1])


for i in range(2, len(nums)):

    dp[i] = max(dp[i-1], dp[i-2] + nums[i])


print(dp[-1])