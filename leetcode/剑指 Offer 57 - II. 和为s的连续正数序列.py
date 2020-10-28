

def findcontinuoussequence(target):
    i, j = 1, 1

    sum = 0
    while i <= target / 2:
        if sum < target:
            sum += j
            j += 1
        elif sum > target:
            sum -= i
            i += 1
        else:
            print(range(i, j))

            sum -= i
            i += 1


if __name__ == '__main__':
    target = int(input())

    findcontinuoussequence(target)
