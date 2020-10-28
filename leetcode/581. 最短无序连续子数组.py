def findMinUnsort(nums):

    length = len(nums)

    maxx = nums[0]

    minn = nums[-1]

    l = 0
    r = -1

    for i in range(length):

        if maxx > nums[i]:
            r = i
        else:
            maxx = nums[i]

        if minn < nums[length - i - 1]:
            l = len - i - l
        else:
            minn = nums[len - i - 1]

    return r - l + 1
