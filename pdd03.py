import re

K = int(input())
a = input().replace(" ", "")
b = input().replace(" ", "")
c = input().replace(" ", "")
d = input().replace(" ", "")
for x in re.finditer(a,c):
for y in re.finditer(b,d):