n = int(input())

res = [[1]]
for i in range(1, n):

    curr = []
    for j in range(i + 1):
       if j == 0:
           curr.append(1)
       elif j == i:
           curr.append(1)
       else:
           curr.append(res[i-1][j-1] + res[i-1][j])

    res.append(curr)

print(res)