

nums = [int(_) for _ in list(input())]


carr = 1

for i in range(len(nums)-1, -1, -1):
    curr = nums[i] + carr

    nums[i] = curr % 10
    carr = curr // 10


if carr > 0:
    nums.insert(0, 1)

print(''.join([str(_) for _ in nums]))

