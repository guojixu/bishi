#
# from functools import cmp_to_key
# def minNum(nums):
#
#     if len(nums) < 1:
#         return ''
#
#     else:
#         compare = cmp_to_key(lambda x, y: int(str(x) + str(y) - int(str(y) + str(x))))
#         # nums.sort(nums, key=compare)
#         nums.sort(nums, key=compare)
#     return ''.join(str(s) for s in nums)
#
# nums = [3,32,321]
# print(minNum(nums))


# -*- coding:utf-8 -*-
from functools import cmp_to_key
class Solution:
    def PrintMinNumber(self, numbers):
        if len(numbers) < 1:
            return ''
        else:
            compare = cmp_to_key(lambda x, y: int(str(x)+str(y))-int(str(y)+str(x)))

            numbers.sort(key=compare)
        return ''.join(str(s) for s in numbers)

s = Solution()
print(s.PrintMinNumber([3,32,321]))

# from functools import cmp_to_key
# lst = [(9, 4), (2, 10), (4, 3), (3, 6)]
#
# def cmp(x, y):
#     a = x[0] if x[0] %2 == 1 else x[1]
#     b = y[0] if y[0] %2 == 1 else y[1]
#
#     return 1 if a > b else -1 if a < b else 0
#
# lst.sort(key=cmp_to_key(cmp))
# print(lst)