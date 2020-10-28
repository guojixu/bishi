

nums = [int(_) for _ in input().split(',')]

i = 0
j = len(nums) - 1
print(nums)
while i < j:

    while i < j and nums[i] % 2 != 0:
        i += 1

    while i < j and nums[j] % 2 == 0:
        j -= 1

    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp
    i += 1
    j += 1


print(nums)