
nums = [int(_) for _ in input().split(',')]

sum = 0

ans = float('-inf')
for x in nums:
    sum += x
    ans = max(ans, sum)
    if sum < 0:
        sum = 0

print(ans)


























