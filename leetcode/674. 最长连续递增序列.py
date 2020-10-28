
nums = [int(_) for _ in input().split(',')]


curr = 1

res = 1
for i in range(len(nums)):

    if nums[i] > nums[i-1]:
        curr += 1
        res = max(res, curr)
    else:
        curr = 1

print(res)