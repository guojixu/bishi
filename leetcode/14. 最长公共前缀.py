strs = input().split(',')
ans = ''
print(list(zip(*strs)))
for i in zip(*strs):
    if len(set(i)) == 1:
        ans += i[0]
    else:
        break

print(ans)


def lcp(start, end):
    if start == end:
        return strs[start]

    mid = (start + end) // 2
    lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
    minLength = min(len(lcpLeft), len(lcpRight))
    for i in range(minLength):
        if lcpLeft[i] != lcpRight[i]:
            return lcpLeft[:i]

    return lcpLeft[:minLength]




# return "" if not strs else lcp(0, len(strs) - 1)
lcp(0, len(strs) - 1)

def my_lcp(start, end):
    if start == end:
        return strs[start]

    mid = (start + end) // 2

    left, right = lcp(start, mid), lcp(mid + 1, end)

    minLen = min(len(left), len(right))

    for i in range(minLen):
        if left[i] != right[i]:
            return left[:i]

    return left[minLen]

def my_lcp2(start, end):
    if start == end:
        return strs[start]

    mid = (start + end) // 2

    left, right = lcp(start, mid), lcp(mid + 1, end)

    minLen = min(len(left), len(right))

    for i in range(minLen):

        if left[i] != right[i]:
            return left[:i]


    return left[minLen]


