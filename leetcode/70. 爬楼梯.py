
n = int(input())

p1 = 0
p2 = 0
p3 = 1

for _ in range(n):

    p1 = p2
    p2 = p3
    p3 = p1 + p2

print(p3)