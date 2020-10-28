n = int(input())

matrix = [[x for x in input().split(',')] for _ in range(n)]

print(matrix)


def maximalSquare(matrix):
    if matrix is None or len(matrix) < 1 or len(matrix[0]) < 1:
        return 0
    height = len(matrix)
    width = len(matrix[0])

    maxSide = 0

    dp = [[0] * (width + 1) for _ in range(height + 1)]

    for i in range(1, height + 1):
        for j in range(1, width + 1):
            if matrix[i - 1][j - 1] == '1':
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j]) + 1
                maxSide = max(maxSide, dp[i][j])

    return maxSide * maxSide


