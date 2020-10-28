class ListNode:
    def __init__(self, val):

        self.val = val

        self.next = None


def showList(head):

    p = head

    while p:
        print(p.val)
        p = p.next

def isPalindrome(head):

    slow, fast = head, head

    new_head = None

    while fast != None and fast.next != None:

        tmp = slow
        slow = slow.next
        fast = fast.next.next

        tmp.next = new_head
        new_head = tmp

    while fast != None:
        fast = fast.next
        slow = slow.next


    fast = new_head

    while slow != None and fast != None:
        if fast.val == slow.val:
            fast = fast.next
            slow = slow.next
        else:
            print('False')
            return
    print('True')
    return

def isHW2(head):


    slow = head
    fast = head

    new_head = None

    while fast != None and fast.next != None:

        tmp = slow
        slow = slow.next
        fast = fast.next.next

        tmp.next = new_head
        new_head = tmp

    while fast:
        fast = fast.next
        slow = slow.next
    while slow!= None and fast != None:

        if fast.val == slow.val:

            fast = fast.next
            slow = slow.next
        else:
            print('False')
            return
    print('True')
    return




def isHW(head):

    slow = head
    fast = head

    new_head = None

    while fast != None and fast.next != None:

        tmp = slow
        slow = slow.next
        fast = fast.next.next

        tmp.next = new_head
        new_head = tmp

    while fast!= None:
        fast = fast.next
        slow = slow.next
    while slow!= None and fast != None:

        if fast.val == slow.val:

            fast = fast.next
            slow = slow.next
        else:
            print('False')
            return
    print('True')
    return


def toList():

    s = [_ for _ in input().split()]
    head = ListNode(s[0])

    p = head

    for x in s[1:]:
        curr = ListNode(x)
        p.next = curr
        p = p.next

    return head

if __name__ == '__main__':
    head = toList()
    isPalindrome(head)