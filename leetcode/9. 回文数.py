s = input()

i = 0
j = len(s) - 1

while i < j:

    if s[i] != s[j]:
        print('false')

        exit(0)
    i += 1
    j -= 1

print('true')

