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

    return head.next

def reverseList_1(head):

    if head == None or head.next == None:
        return head
    p = reverseList_1(head.next)
    head.next.next = head
    head.next = None

    return p

def reverseList_2(head):

    if head == None or head.next == None:
        return head

    p = head
    new_head = None
    while p != None:

        tmp = p
        p = p.next
        tmp.next = new_head
        new_head = tmp

    return new_head


def printList(head):

    p = head
    while p != None:
        print(p.val, end=' ')
        p = p.next
    print()

def oddEvenList(head):

    if head == None:
        return None

    odd = head
    even = head.next
    evenHead = head.next


    while even != None and even.next != None:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = evenHead


    return head



if __name__ == '__main__':
    head = toListNode()
    printList(head)
    head = reverseList_1(head)
    printList(head)
    head = reverseList_2(head)
    printList(head)

    head_odd = oddEvenList(head)

    printList(head_odd)