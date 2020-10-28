

def sortList(head):


    if not head or head.next == None:
        return head

    slow, fast = head, head.next

    while fast and fast.next:

        fast, slow = fast.next.next, slow.next

    mid, slow.next = slow.next, None

    left, right = sortList(head), sortList(mid)

    h = res = ListNode(0)

    while left and right:
        if left.val < right.val:
            h.next, left = left, left.next
        else:
            h.next, right = right, right.next
    h.next = left if left else right

    return res.next

