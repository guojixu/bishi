
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def toListNode():
    s = input().split()


    head = ListNode(-1)
    p = head
    for x in s:
        p.next = ListNode(x)
        p = p.next

    return head

def reversePrint(head):
    if head == None:
        return
    reversePrint(head.next)
    print(head.val)
if __name__ == '__main__':
    head = toListNode()
    reversePrint(head.next)
