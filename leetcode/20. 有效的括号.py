
from collections import deque

s = input()

stack = []

for x in s:
    if x in ['(', '[', '{']:
        stack.append(s)
    elif x == ')':
        if stack[-1] == '(':
            stack.pop()
        else:
            print("false")
            exit(0)
    elif x == ']':
        if stack[-1] =='[':
            stack.pop()
        else:
            print('False')
            exit(0)
    elif x == '}':
        if stack[-1] == '{':
            stack.pop()
        else:
            print('False')
            exit(0)



print('True')