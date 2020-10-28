class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


s = input().split()
target = int(input())


head = ListNode(-1)

p = head

for val in s:
    p.next = ListNode(val)
    p = p.next

p = head
for _ in range(target):
    p = p.next

q = head

while p != None:
    p = p.next

    q = q.next

print(q.val)
