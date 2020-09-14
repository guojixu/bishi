#2
n, m = [int(_) for _ in input().split()]

nums = [[i] for i in range(n)]
groups = {i: i for i in range(n)}
idx = {i: 0 for i in range(n)}
for _ in range(m):
    ch, a, b = input().split()
    a = int(a) - 1
    b = int(b) - 1
    if ch == "C":
        tmp = nums[a][:]
        nums[a].clear()
        k = len(nums[b])
        nums[b].extend(tmp)
        for i, x in enumerate(tmp):
            groups[x] = b
            idx[x] = k + i
    else:
        if groups[a] == groups[b]:
            print(abs(idx[a] - idx[b]) - 1)
        else:
            print(-1)
