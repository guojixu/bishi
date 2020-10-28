


def findKlag(nums, k, left, right):

    p = partition(nums, left, right)
    if p == k - 1:
        return nums[p]

    elif p < k - 1:
        return findKlag(nums, k, p + 1, right)
    else:
        return findKlag(nums, k, left, p - 1)


def quickSort(nums, left, right):

    if left < right:
        p = partition(nums, left, right)
        quickSort(nums, left, p-1)
        quickSort(nums, p+1, right)

def partition(nums, left, right):

    curr = nums[right]

    i = left
    j = right

    while i < j:
        while i < j and nums[i] >= curr:
            i += 1
        nums[j] = nums[i]
        while i < j and nums[j] <= curr:
            j -= 1
        nums[i] = nums[j]

    nums[i] = curr

    return i


def quickSort2(nums, left, right):
    if left < right:
        p = partition2(nums, left, right)

        quickSort2(nums, left, p - 1)
        quickSort2(nums, p + 1, right)
def partition2(nums, left, right):

    curr = nums[right]

    i = left
    j = right
    while i < j:

        while i < j and nums[i] >= curr:
            i += 1
        nums[j] = nums[i]

        while i < j and nums[j] <= curr:
            j -= 1
        nums[i] = nums[j]

    nums[i] = curr

    return i


if __name__ == '__main__':
    nums = [int(_) for _ in input().split(',')]
    # k = int(input())
    # res = findKlag(nums, k, 0, len(nums) - 1)
    # print(res)

    quickSort2(nums, 0, len(nums) - 1)
    print(nums)