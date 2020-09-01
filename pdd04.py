N, M = [int(_) for _ in input().split()]
nums = []
for _ in range(M):
    nums.append(int(input()))

from itertools import combinations


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lcm(*nums):
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return nums[0] * nums[1] // gcd(nums[0], nums[1])
    return lcm(lcm(*nums[:-1]), nums[-1])

ans = 0
for k in range(M):
    perms = combinations(nums, k + 1)
    s = 0
    for perm in perms:
        s += N // lcm(*perm)
    ans += (-1) ** k * s
print(ans)
