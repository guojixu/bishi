class Solution:
    def mergeSort(self, nums, tmp, l, r):
        if l >= r:
            return 0
        mid = (l + r) // 2

        inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)

        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inv_count += (j - (mid + 1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            inv_count += (j - (mid + 1))
            pos += 1
        for k in range(j, r + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l:r + 1] = tmp[l:r + 1]
        return inv_count

    def mergesort2(self, nums, tmp, l, r):

        if l >= r:
            return 0

        mid = (l + r) // 2

        count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)

        i = l
        j = mid + 1

        p = l

        while i <= mid and j <= r:

            if nums[i] <= nums[j]:
                tmp[p] = nums[i]
                i += 1
                count += (j - (mid + 1))
            else:
                tmp[p] = nums[j]
                j += 1
            p += 1

        for k in range(i, mid + 1):
            tmp[p] = nums[k]
            count += (j - (mid + 1))
            p += 1
        for k in range(j, r + 1):
            tmp[p] = nums[k]

        nums[l:r+1] = tmp[l:r+1]

        return count


    def reversePairs(self, nums) -> int:
        n = len(nums)
        tmp = [0] * n
        return self.mergeSort(nums, tmp, 0, n - 1)


sol = Solution()

print(sol.reversePairs(nums=[7, 5, 6, 4]))
