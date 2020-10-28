nums = [int(_) for _ in input().split(',')]
k = int(input())

n = len(nums)

left = [0] * n
left[0] = nums[0]
right = [0] * n
right[-1] = nums[-1]

for i in range(1, n):
    if i % k == 0:
        left[i] = nums[i]
    else:
        left[i] = max(left[i - 1], nums[i])

    j = n - i - 1

    if (j + 1) % k == 0:
        right[j] = nums[j]
    else:
        right[j] = max(right[j + 1], nums[j])

print(left)
print(right)

res = []

for i in range(n - k + 1):
    res.append(max(left[i + k - 1], right[i]))

print(res)
