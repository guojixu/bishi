
nums = [int(_) for _ in input().split(',')]

for num in nums:

    index = abs(num) - 1
    nums[index] = -abs(nums[index])

for i in range(len(nums)):

    if nums[i] > 0:
        print(i+1, end=',')

print('')