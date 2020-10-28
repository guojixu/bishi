

def reverse(x):

    res = 0

    flag = 1

    if x < 0:
        flag = -1
    x = abs(x)

    while x > 0:

        curr = x % 10

        tmp = res * 10 + curr

        if (tmp - curr) // 10 != res:
            return 0

        res = tmp

        x = x // 10
    return flag * res

print(reverse(-123))