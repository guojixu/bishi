valueDict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

s = input()

sum = 0

preNum = valueDict.get(s[0])
for x in list(s[1:]):

    currNum = valueDict.get(x)

    if preNum < currNum:
        sum -= preNum
    else:
        sum += preNum

    preNum = currNum

sum += preNum
print(sum)

