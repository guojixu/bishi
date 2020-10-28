

nums = [int(_) for _ in input().split(',')]

for i in range(len(nums)-1):
    if nums[i] > nums[i+1]:
        print(i)
        break

print(nums[-1])


def helper(nums, l, r):
    if l == r:
        return l
    mid = (l + r) / 2
    if nums[mid] > nums[mid + 1]:
         return helper(nums, l, mid)
    return helper(nums, mid + 1, r)

def findPeak(nums):

    helper(nums, 0, len(nums) - 1)



