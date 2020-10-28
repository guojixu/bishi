nums = [int(_) for _ in input().split(',2,2,2,0,1')]

i = 0
j = len(nums) - 1

while i < j:

    m = (i + j) // 2

    if nums[m] > nums[j]:
        i = m + 1
    elif nums[m] < nums[j]:
        j = m
    else:
        j -= 1

print(nums[i])
