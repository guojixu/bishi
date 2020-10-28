

nums = [int(_) for _ in input().split()]

nums = sorted(nums)
# print(nums)

n = len(nums)
res = []

i = 0
while i < n - 1:

    left = i + 1
    right = n - 1

    while left < right:

        if left < right and nums[i] + nums[left] + nums[right] < 0:
            left += 1
        elif left < right and nums[i] + nums[left] + nums[right] > 0:
            right -= 1

        else:
            # print(i, left, right)
            res.append([nums[i], nums[left], nums[right]])
            left += 1

            while left < right and nums[left] == nums[left-1]:
                left += 1

            right -= 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1


        while i < n - 2 and nums[i + 1] == nums[i]:
            i += 1

    i += 1

for curr in res:
    print(' '.join([str(_) for _ in curr]))