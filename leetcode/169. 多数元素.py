
nums = [int(_) for _ in input().split(',')]

vote = 0
res = 0

for n in nums:
    if vote == 0:
        res = n
    vote = vote + (1 if n == res else -1)
print(res)