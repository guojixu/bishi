

nums = [int(_) for _ in input().split()]

def permute(nums):

    res = []

    def helper(nums, curr):

        if not nums:
            res.append(curr)
            return
        for i in range(len(nums)):

            
            helper(nums[:i] + nums[i+1:], curr + [nums[i]])

    helper(nums, [])

    return res

print(permute(nums))
from itertools import permutations
print(list(permute(nums)))


def permute(nums):

    res = []


    def helper(nums, curr):
        if not nums:
            res.append(curr)
            return
        for i in range(len(nums)):
            helper(nums[:i] + nums[i+1:], curr + [nums[i]])


    helper(nums, [])

    return res


