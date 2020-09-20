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


import copy
 
 
def calculate_add_combination_4_num(n):
    res_list = []
    tmp_list = []
 
    def num_to_n(n,tmp_list, start):
        if n == 1:
            tmp = copy.deepcopy(tmp_list)
            tmp.append(1)
            res_list.append(tmp)
        else:
            for i in range(start,n):
                tmp_list.append(i)
                num_to_n(n-i,tmp_list,i)
                tmp_list.remove(tmp_list[-1])
 
            tmp = copy.deepcopy(tmp_list)
            tmp.append(n)
            res_list.append(tmp)
 
    num_to_n(n,tmp_list, 1)
    # duplicate remove
    return res_list
 

