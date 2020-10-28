class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def toList():
    s = input().split()

    head = ListNode(-1)
    p = head
    for val in s:
        p.next = ListNode(val)
        p = p.next

    return head


def my_reverse_1(head):
    if head == None or head.next == None:
        return head
    p = my_reverse_1(head.next)
    head.next.next = head
    head.next = None
    return p



def my_reverse_2(head):
    if head == None or head.next == None:
        return None

    new_head = None

    while p != None:
        tmp = p
        p = p.next

        tmp.next = new_head
        new_head = tmp

    return new_head



#
# def reverse(head, tail):
#     if head == None or head.next == None:
#         return head
#
#     pre = tail.next
#
#     p = head
#
#     while pre != tail:
#         next = p.next
#         p.next = pre
#         pre = p
#         p = next
#
#     return tail, head


def k_reverse(head, k):
    if head == None or head.next == None:
        return None

    tail = head

    for i in range(k):

        if tail == None:
            return head
        tail = tail.next

    new_head = reversed(head, tail)

    head.next = k_reverse(tail, k)

    return new_head


def reverseKGroup(head,k):

    if head == None or head.next == None:
        return head
    tail = head
    for i in range(k):
        if tail == None:
            return head
        tail = tail.next
    newHead = my_reverse_22(head, tail)
    head.next = reverseKGroup(tail, k)

    return newHead


def reverse(head, tail):
    new_head = None
    p = None
    while head != tail:

        p = head.next
        head.next = new_head

        new_head = head
        head = p
    return new_head

def my_reverse_22(head, tail):

    if head == None or head.next == None:
        return head

    p = head
    new_head = tail

    while p != tail:

        tmp = p
        p = p.next

        tmp.next = new_head

        new_head = tmp

    return new_head



def my_reverse_2(head, tail):

    if head == None or head.next == None:
        return None

    pre = head

    new_head = None

    while p != tail:

        tmp = p
        p = p.next

        tmp.next = new_head
        new_head = tmp

    return new_head




def showList(head):
    p = head
    while p != None:
        print(p.val)
        p = p.next


if __name__ == '__main__':
    head = toList()
    k = int(input())
    # k_reverse(root, k)
    showList(head.next)
    new_head = reverseKGroup(head.next, k)
    showList(new_head)