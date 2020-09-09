import re

K = int(input())
a = input().replace(" ", "")
b = input().replace(" ", "")
N = int(input())
c = input().replace(" ", "")
d = input().replace(" ", "")
s1, s2 = set(), set()
for x in re.finditer(a, c):
    s1.add(x.start())
for y in re.finditer(b, d):
    s2.add(y.start())
ans = s1 & s2
if not ans:
    print(0)
else:
    print(min(ans)+1)

# 3
# 1 2 3
# 3 2 1
# 6
# 1 2 1 2 3 3
# 5 4 3 2 1 1

