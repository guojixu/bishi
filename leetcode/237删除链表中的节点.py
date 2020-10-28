
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

s = [int(_) for _ in input().split()]

target = int(input())

head = ListNode(-1)
p = head
for x in s:
    p.next = ListNode(x)
    p = p.next

p = head


p = head.next
pre = head

while p != None and p.val != target:

    pre = p
    p = p.next

if p != None:
    pre.next = p.next
    del p

p = head
while p != None:
    print(p.val)
    p = p.next


