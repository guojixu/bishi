def kmp(mom_string, son_string):
    pos1 = []
    test = ''
    if type(mom_string) != type(test) or type(son_string) != type(test):
        pos1.append(-1)
        return pos1
    if len(son_string) == 0:
        pos1.append(0)
        return pos1
    if len(mom_string) == 0:
        pos1.append(-1)
        return pos1
    next = [-1] * len(son_string)
    if len(son_string) > 1:
        next[1] = 0
        i, j = 1, 0
        while i < len(son_string) - 1:
            if j == -1 or son_string[i] == son_string[j]:
                i += 1
                j += 1
                next[i] = j
            else:
                j = next[j]
    m = s = 0
    while (s < len(son_string) and m < len(mom_string)):
        if s == -1 or mom_string[m] == son_string[s]:
            m += 1
            s += 1
        else:
            s = next[s]

    if s == len(son_string):
        pos1.append(m - s)
    pos1.append(-1)
    return pos1


k = int(input())
pat1 = "".join(input().strip().split())
pat2 = "".join(input().strip().split())
n = int(input())
st1 = "".join(input().strip().split())
st2 = "".join(input().strip().split())

pos11 = kmp(st1, pat1)
pos22 = kmp(st2, pat2)
k = [i for i in pos11 if i in pos22 and i != -1]
if len(k) == 0:
    print(0)
else:
    print(k[0] + 1)