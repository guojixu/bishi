


n = int(input())



# l = 0.0000
# r = float(n)
#
# ans = 0
# while l <= r:
#     print(l, r)
#     m = (l + r) / 2
#     if m * m <= n:
#         ans = m
#         l = m + 1
#     else:
#         r = m - 1
#
# print(ans)
x = n

C, x0 = float(x), float(x)
while True:
    xi = 0.5 * (x0 + C / x0)
    if abs(x0 - xi) < 1e-7:
        break
    x0 = xi

print(x0)


c, x0 = float(x), float(x)
while True:
    xi = 0.5 * (x0 + c / x0)
    if abs(x0 - xi) < 1e-7:
        break
    x0 = xi
print(x0)