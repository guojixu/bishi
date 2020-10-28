
# 用dp的方法
# dp[i][j]表示A[0, i],B[0, j]最长公共子串

# 如果相等dp[i][j] = dp[i-1][j-1] + 1
# 否则dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# m, n = len(text1), len(text2)
#
# dp = [[0] * (n + 1) for _ in range(m + 1)]
#
# for i in range(1, m + 1):
#     for j in range(1, n + 1):
#         if text1[i - 1] == text2[j - 1]:
#             dp[i][j] = 1 + dp[i - 1][j - 1]
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
# return dp[-1][-1]

def maxsubstr(str1, str2):

    m, n = len(str1), len(str2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m+1):
        for j in range(1, n+1):

            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]

print(maxsubstr("abcde", "ace"))