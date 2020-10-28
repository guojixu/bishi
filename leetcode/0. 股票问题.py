
# 股票1：只买卖一次
def maxProfit(prices) -> int:
    if len(prices) == 0:
        return 0
    s0 = 0
    s1 = float('-inf')
    s2 = float('-inf')

    for p in prices:
        s0, s1, s2 = s0, max(s0 - p, s1), max(s1 + p, s2)

    return max(s0, s2)

# 股票2：无限买卖

def maxProfit(prices) -> int:
    s0 = 0
    s1 = float('-inf')
    s2 = float('-inf')

    for p in prices:
        # s0, s1, s2 = s0, max(s0, s)
        s0, s1 = max(s0, s1 + p), max(s1, s0-p)
        # s0, s1, s2 = s0, max(s0-p, s1, s2 - p), max(s1 - p, s2)
    return max(s0, s1, s2)

# 股票3：买卖两次
def maxProfit(prices) -> int:

        if len(prices) == 0:
            return 0

        s0 = 0
        s1 = float('-inf')
        s2 = float('-inf')
        s3 = float('-inf')
        s4 = float('-inf')

        for p in prices:
            s0 = s0
            s1, s2, s3, s4 = max(s1, s0-p), max(s2, s1 + p), max(s3, s2 - p), max(s4, s3 + p)

        return max(s0, s1, s2, s3, s4)

# 股票4：买卖k次
def maxProfit(k, prices) -> int:

    n = len(prices)

    if k >= n // 2:
        return sum(max(0, prices[i] - prices[i-1]) for i in range(1, n))

    s = [float('-inf') for _ in range(2*k + 1)]
    s[0] = 0
    for i in range(n):
        for j in range(k):
            s[2*j + 1], s[2*j + 2] = max(s[2*j+1], s[2*j] - prices), max(s[2*j + 2], s[2*j + 1] + prices[i])


    return max(s[2*j] for j in range(k + 1)) if n else 0

# 含有冷冻期

def maxProfit(prices) -> int:


    s0 = 0
    s1 = float('-inf')
    s2 = float('-inf')

    for p in prices:
        s0, s1, s2 = max(s0, s2), max(s0 - p, s1), s1 + p
    return max(s0, s2)

# 含有手续费

def maxProfit(prices, fee) -> int:


    n = len(prices)

    s0, s1 = 0, float('-inf')

    for p in prices:
        s0, s1 = max(s0, s1 + p - fee), max(s1, s0-p)

    return s0

# 打家劫舍，不能相邻

def rob(nums) -> int:
    s0, s1, s2 = 0, float('-inf'), float('-inf')

    for num in nums:
        s0, s1, s2 = s0, max(s0 + num, s2 + num), max(s2, s1)

    return max(s0, s1, s2)