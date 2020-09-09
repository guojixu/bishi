N = int(input())

w = [0] * (N + 1)

lc, rc = [-1] * (N + 1), [-1] * (N + 1)

root = None

for _ in range(N):
    id, weight, left, right = [int(_) for _ in input().split()]

    w[id] = weight

    lc[id] = left
    rc[id] = right


def dfs(root, prev):
    if root == -1:
        return prev

    if w[root] ^ prev < prev:
        return prev

    prev = w[root] ^ prev

    return max(dfs(lc[root], prev), dfs(rc[root], prev))


print(max(dfs(root, 0) for root in range(1, N + 1)))