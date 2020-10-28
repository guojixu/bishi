


nums = [int(_) for _ in input().split(',')]
target = int(input())



i = 0
j = len(nums) - 1

while i < j:

    if nums[i] + nums[j] == target:
        print(nums[i], nums[j])
        i += 1
    elif nums[i] + nums[j] > target:
        j -= 1
    else:
        i += 1

# from collections import Counter
#
# print(Counter('leetcode'))
# print(list(enumerate('leetcode')))

