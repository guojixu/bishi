

def maxSubSum(nums):

    sum = 0
    res = float('-inf')

    for x in nums:
        # sum < 0的话就让sum = x
        if sum < 0:
            sum = x
        else:
            sum += x

        res = max(res, sum)

    return res