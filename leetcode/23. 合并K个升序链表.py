def mergeK(lists):
    return helper(lists, 0, len(lists))


def helper(lists, left, right):
    if left == right:
        return lists[left]

    mid = (left + right) // 2

    l1 = helper(lists, left, mid)
    l2 = helper(lists, mid + 1, right)

    return merge(l1, l2)


def merge(l1, l2):
    if l1 == None:
        return l2
    if l2 == None:
        return l1

    if l1.val < l2.val:
        l1.next = merge(l1.next, l2)
        return l1

    if l2.val < l1.val:
        l2.next = merge(l1, l2.next)


def helper(lists, left, right):

    if left == right:
        return lists[left]

    mid = (left + right) // 2

    l1 = helper(lists, left, mid)
    l2 = helper(lists, mid + 1, right)

    return merge(l1, l2)

