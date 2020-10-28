

heights = [int(_) for _ in input().split(',')]

# 双指针
# 0,1,0,2,1,0,1,3,2,1,2,1

n = len(heights)
max_left= [0] * n
max_right = [0] * n

max_left[0] = heights[0]

for i in range(1, n):
    max_left[i] = max(max_left[i-1], heights[i])

max_right[n-1] = heights[n-1]
for i in range(n-2, -1, -1):
    max_right[i] = max(max_right[i+1], heights[i])

# print(list(range(n-1, -1, -1)))
#
# print(max_left, max_right)
ans = 0
for i in range(1, n):
    currmin = min(max_left[i], max_right[i])


    ans += (currmin - heights[i]) if currmin > heights[i] else 0


print(ans)








