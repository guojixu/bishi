


def comb():

    nums = [int(_) for _ in input().split()]
    target = int(input())
    res = []

    def helper(nums, start, curr, target):
        # print(curr, 'curr')
        if sum(curr) == target:
            res.append(curr)
            return
        else:
            for i in range(start, len(nums)):
                helper(nums, start + 1, curr + [nums[i]], target)
    helper(nums, 0, [], target)

    print(res)

def combin():

    nums = [int(_) for _ in input().split()]

    target = int(input())

    res = []


    def helper(nums, start, curr, target):
        if sum(curr) == target:
            res.append(curr)
            return
        else:
            for i in range(start, len(nums)):
                help(nums, start + 1, curr + [nums[i]], target)

    helper(nums, 0, [], target)
