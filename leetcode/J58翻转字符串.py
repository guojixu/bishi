
s = input()
n = int(input())
l = len(s)

n = n % l

str1 = s[:n]
str2 = s[n:]

res = str2 + str1

print(res)
