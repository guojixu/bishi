

s = input()

#
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # 哈希集合，记录每个字符是否出现过
#         occ = set()
#         n = len(s)
#         # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
#         rk, ans = -1, 0
#         for i in range(n):
#             if i != 0:
#                 # 左指针向右移动一格，移除一个字符
#                 occ.remove(s[i - 1])
#             while rk + 1 < n and s[rk + 1] not in occ:
#                 # 不断地移动右指针
#                 occ.add(s[rk + 1])
#                 rk += 1
#             # 第 i 到 rk 个字符是一个极长的无重复字符子串
#             ans = max(ans, rk - i + 1)
#         return ans
#


windows = set()

n = len(s)

r = 0
ans = 0


# 双指针



for i in range(n):
    if i != 0:
        windows.remove(s[i-1])
    while r < n and s[r] not in windows:
        windows.add(s[r])
        r += 1
    ans = max(ans, r-i)
print(ans)


def lenlongest(s):

    n = len(s)
    i = 0
    j = 0

    myset = set()
    res = 0

    while i < n and j < n:
        if not myset.__contains__(s[i]):
            set.add(s[i])
            i += 1
        else:
            set.remove(s[j])
            j += 1

        res = max(res, i - j)

    return res