

s = input().split()

res = [[]]

for x in s:
    res = res + [[x] + num for num in res]
print(res)

res = [[]]

for x in s:
    res = res + [[x] + num for num in res]

print(res)


for x in s:
    res = res + [[x] + num for num in res]
print(res)
