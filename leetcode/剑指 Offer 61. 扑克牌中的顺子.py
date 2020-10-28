
nums = [int(_) for _ in input().split(',')]

sorted(nums)

count = 0

while nums[count] == 0:
    count+=1



for i in range(count +1, len(nums)):

    diff = nums[i] - nums[i - 1]
    count = count - diff + 1

    if count < 0 or diff == 0:
        print('false')
        exit(0)

for i in range(count + 1, len(nums)):
    diff = nums[i] - nums[i-1]

    count = count - diff + 1

    if count < 0 or diff == 0:
        print('false')
        exit(0)

print('true')