import heapq
import datetime
from collections import defaultdict

n, m = [int(_) for _ in input().split()]
mp = defaultdict(list)
print(list(mp))
for _ in range(m):
    u, v, time = [int(_) for _ in input().split()]
    mp[u].append((v, time))
    mp[v].append((u, time))
s, e, start = input().split()
s, e = int(s), int(e)

print(mp)

def dijkstra():


    # 未选中

    unselected = [(0, s)]

    # dist表示s到其他点的最短距离

    selected = {}

    # 循环遍历未选中
    while unselected:
        # 找到最小的距离的点

        d, node = heapq.heappop(unselected)


        if node in selected:

            continue

        # 加入到selected

        selected[node] = d

        if node == e:
            return selected[node]

        for nei, d2 in mp[node]:
            if nei not in selected:
                heapq.heappush(unselected, (d + d2, nei))

    return -1
    # return dist[e]

def djst():

    unselected = [(0, s)]

    selected = {}

    while unselected:

        d, node = heapq.heappop(unselected)

        if node in selected:
            continue

        selected[node] = d

        if node == e:
            return

        for nei, d2 in mp[node]:

            if nei not in selected:

                heapq.heappush(unselected, (d+d2, nei))

    return -1




def dj():


    unselected = [(0, s)]

    selected = {}

    while unselected:


        dist, node = heapq.heappop(unselected)

        if node in selected:
            continue

        selected[node] = dist

        if node == e:
            return dist[node]

        for v, vw in mp[node]:
            if v not  in selected:
                heapq.heappush(unselected, (d + vw, v))
    return -1


cur_year = "2020"
hours = dijkstra()
d = datetime.datetime.strptime(cur_year + "/" + start, "%Y/%m.%d/%H")
delta = datetime.timedelta(hours=hours)
d += delta
# print(datetime.datetime.strftime(d, "%-m.%-d/%H"))
print("{}.{}/{}".format(d.month, d.day, d.hour))

'''
4 4
1 2 5
1 3 6
2 4 8
3 4 6
1 4 7.9/8

7.9/20

'''