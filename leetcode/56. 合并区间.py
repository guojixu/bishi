

tmp = [_ for _ in input().split(' ')]

nums = [_.split(',') for _ in tmp]

nums.sort(key=lambda x: x[0])

print(nums)

merged = []

for pair in nums:

    if not merged or merged[-1][1] < pair[0]:
        merged.append(pair)
    else:
        merged[-1][1] = max(merged[-1][1], pair[1])

# [[1,3][2,6],[8,10],[15,18]]
# 1,3 2,6 8,10 15,18

print(merged)


for pair in nums:

    if not merged or merged[-1][1] < pair[0]:
        merged.append(pair)
    else:
        merged[-1][1] = max(merged[-1][1], pair[1])
