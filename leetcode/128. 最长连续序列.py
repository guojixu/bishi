












def longestConsecutive(nums):

    longest_streak = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

def longestConsecutive2(nums):
    hash_dict = dict()

    max_length = 0
    for num in nums:
        if num not in hash_dict:
            left = hash_dict.get(num - 1, 0)
            right = hash_dict.get(num + 1, 0)

            cur_length = 1 + left + right
            if cur_length > max_length:
                max_length = cur_length

            hash_dict[num] = cur_length
            hash_dict[num - left] = cur_length
            hash_dict[num + right] = cur_length

    return max_length


def longest(nums):

    hash_dict = {}

    max_len = 0

    for num in nums:

        if num not in hash_dict:

            left = hash_dict.get(num - 1, 0)
            right = hash_dict.get(num + 1, 0)

            curr_len = 1 + left + right

            if curr_len > max_len:
                max_len = curr_len

            hash_dict[num] = curr_len
            hash_dict[num + right] = curr_len
            hash_dict[num - left] = curr_len
    return max_len

nums = [int(_) for _ in input().split(',')]
print(longest(nums))