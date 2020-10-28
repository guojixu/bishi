
nums = [int(_) for _ in input().split(',')]
target = int(input())

i = 0
j = len(nums) - 1

while i <= j:
    m = (i + j) // 2

    if nums[m] <= target:
        i = m + 1
    else:
        j = m - 1

right = i

if j >= 0 and nums[j] != target:
    print('no')
    exit(0)

i = 0
j = len(nums) - 1

while i <= j:
    m = (i + j) // 2
    if nums[m] < target:
        i = m + 1
    else:
        j = m - 1

left = j

print(right - left - 1)
