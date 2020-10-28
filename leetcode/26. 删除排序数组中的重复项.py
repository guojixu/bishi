

nums = [int(_) for _ in input().split(',')]

i = 0

for j in range(len(nums)):

    if nums[i] != nums[j]:
        i += 1
        nums[i] = nums[j]


print(i+1)