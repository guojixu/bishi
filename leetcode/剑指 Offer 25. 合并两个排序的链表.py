class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def toList():
    s = [int(_) for _ in input().split()]

    head = ListNode(s[0])

    p = head

    for x in s:
        p.next = ListNode(x)
        p = p.next

    return head.next

def merge(l1, l2):

    head = ListNode(-1)
    p = head
    while l1 != None and l2 != None:

        if l1.val < l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2

            l2 = l2.next
        p = p.next

    return head.next


def printList(head):
    p = head
    while p != None:
        print(p.val)
        p = p.next

if __name__ == '__main__':
    l1 = toList()
    l2 = toList()
    l3 = merge(l1, l2)
    printList(l3)

