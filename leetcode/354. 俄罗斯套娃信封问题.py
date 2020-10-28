
# 算法思路：
# 首先按照w进行升序，对h进行降序
# 然后对h进行最长子序列

def max_envelopes(envs):
    envs = sorted(envs, key=lambda x:(x[0], -x[1]))

    print(envs)
    h = [env[1] for env in envs]

    def lis(h):
        res = 0

        len_h = len(h)

        if len_h == 0:
            return 0

        dp = [1] * len_h

        for i in range(len_h):
            for j in range(i):
                if h[j] < h[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res

    print(lis(h))

envs = [[5,4],[6,4],[6,7],[2,3]]

max_envelopes(envs)