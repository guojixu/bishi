
from collections import Counter

nums1 = [int(_) for _ in input().split()]
nums2 = [int(_) for _ in input().split()]

m = Counter()

for x in nums1:
    m[x] += 1

res = []
for x in nums2:

    count = m.get(x, 0)
    if count > 0:
        res.append(x)
        m[x] -= 1

        if m[x] == 0:
            m.pop(x)

print(res)