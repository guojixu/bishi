


nums = [int(_) for _ in input().split(',')]

target = int(input())


def search(nums, target):


    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[left]:

            if target >= nums[left] and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:

            if target > nums[mid] and target <= nums[right]:

                left = mid + 1
            else:
                right = mid - 1


    return -1


print(search(nums, target))
