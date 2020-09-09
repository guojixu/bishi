res = 0
from collections import defaultdict


def dfs(u, path: list):
    global res
    x = w[u]
    res = max(res, x)
    for i in range(len(path) - 1, -1, -1):
        x ^= w[i]
        res = max(res, x)
    path.append(w[u])
    for v in mp[u]:
        dfs(v, path)
    path.pop()


N = int(input())
w = [0] * (N + 1)
mp = defaultdict(list)
has_father = [False] * (N + 1)
for _ in range(N):
    id, weight, left, right = [int(_) for _ in input().split()]
    w[id] = weight
    if left != -1:
        mp[id].append(left)
        has_father[left] = True
    if right != -1:
        mp[id].append(right)
        has_father[right] = True

root = None
for i in range(1, N + 1):
    if not has_father[i]:
        root = i
        break
path = []
dfs(root, path)
print(res)
