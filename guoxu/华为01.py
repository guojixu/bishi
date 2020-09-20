import re

K = int(input())
a = input().replace(" ", "")
b = input().replace(" ", "")
N = int(input())
c = input().replace(" ", "")
d = input().replace(" ", "")
s1, s2 = set(), set()

# print(list(re.finditer(a, c)))
# for x in re.finditer(a, c):
#     s1.add(x.start())
#
# print(s1)
# for y in re.finditer(b, d):
#     s2.add(y.start())
#
#
# print(s2)
# ans = s1 & s2
# if not ans:
#     print(0)
# else:
#     print(min(ans)+1)


'''
3
1 2 3
3 2 1
6
1 2 1 2 3 3
5 4 3 2 1 1

3

'''

new_sub = ''
for x, y in zip(a,b):
    new_sub += x
    new_sub += y

new_s = ''
for x, y in zip(c, d):
    new_s += x
    new_s += y

print(new_sub, new_s)
print((new_s.find(new_sub) // 2)+1)


# 3
# 2 3 3
# 4 3 2
# 6
# 1 2 1 2 3 3
# 5 4 3 2 1 1