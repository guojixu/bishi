n = int(input())
matrix = [[x for x in input().split(',')] for _ in range(n)]

print(matrix)

# res = []
#
# while matrix:
#
#     res += matrix.pop(0)
#
#     matrix = list(zip(*matrix))[::-1]
#


dirs = [[0,1],[1,0],[0,-1],[-1,0]]

res = []

count = 0

row = 0
col = 0

dirIndex = 0

while count < n**2:


    res.append(matrix[row][col])

    matrix[row][col] = -1000

    next_row, next_col = row + dirs[dirIndex][0], col + dirs[dirIndex][1]

    if not (0 <= next_row < n and 0 <= next_col < n and matrix[next_row][next_col] != -1000):


        dirIndex = (dirIndex + 1) % 4

    row += dirs[dirIndex][0]
    col += dirs[dirIndex][1]

    count += 1

print(res)

