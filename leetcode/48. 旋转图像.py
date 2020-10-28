
# import sys
#
# matrix = []
# for line in sys.stdin:
#
#     matrix.append(line.split())


matrix = []

N = int(input())
for _ in range(N):

    matrix.append(input().split())


def rotate(matrix):

    n = len(matrix[0])
    # transpose matrix
    for i in range(n):
        for j in range(i, n):
            print(i, j)

            print(matrix[j][i], matrix[i][j])
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    print(matrix)

    for i in range(n):
        matrix[i].reverse()

    print(matrix)

rotate(matrix)

'''
3
1 2 3
4 5 6
7 8 9
'''

# print(matrix)
