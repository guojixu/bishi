nums = [int(_) for _ in input().split(',')]

i = 0
j = 0

idx = 0

for n in nums:
    if n != 0:
        nums[idx] = n
        idx += 1

for _ in range(idx, len(nums)):
    nums[_] = 0

print(nums)