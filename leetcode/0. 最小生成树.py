from collections import defaultdict
import heapq


def prim():
    vis = set()
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        e, u = heapq.heappop(q)
        if u in vis:
            continue
        if e > k:
            return False
        vis.add(u)
        for v, w in mp[u]:
            if v not in vis:
                heapq.heappush(q, (w,v))
    if len(vis) == n:
        return True
    else:
        return False

T = int(input())
for _ in range(T):
    n, m, k = [int(_) for _ in input().split()]
    mp = defaultdict(list)
    for _ in range(m):
        u, v, w = [int(_) for _ in input().split()]
        mp[u].append((v, w))
        mp[v].append((u, w))
    if prim():
        print("Yes")
    else:
        print("No")

