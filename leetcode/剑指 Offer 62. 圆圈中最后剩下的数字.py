



n = int(input())
m = int(input())

nums = [_ for _ in range(n)]

idx = 0
while len(nums) > 1:
    idx = (idx + m - 1) % n
    nums.pop(idx)

    n -= 1

print(nums[0])

