

from collections import deque

class TreeNode:
    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None


def toTree():

    s = [_ for _ in input().split(',')]

    root = TreeNode(int(s[0]))

    myQ = deque()

    myQ.appendleft(root)

    curr_index = 1

    while curr_index < len(s):

        currNode = myQ.pop()

        currVal = s[curr_index]
        curr_index += 1

        if currVal != 'null':
            currNode.left = TreeNode(int(currVal))
            myQ.appendleft(currNode.left)

        if curr_index > len(s):
            break

        currVal = s[curr_index]
        curr_index += 1

        if currVal != 'null':
            currNode.right = TreeNode(int(currVal))
            myQ.appendleft(currNode.right)



    return root


def inorder(root):

    if root == None:
        return

    inorder(root.left)

    print(root.val)

    inorder(root.right)


def levelOrder(root):

    myQ = deque()

    myQ.appendleft(root)

    res = []

    while len(myQ) > 0:

        currList = []

        currQ = deque()

        while len(myQ) > 0:

            currNode = myQ.pop()

            currList.append(int(currNode.val))

            if currNode.left != None:
                currQ.appendleft(currNode.left)

            if currNode.right != None:
                currQ.appendleft(int(currNode.right))

        res.append(currList)

        while len(currQ) > 0:
            myQ.appendleft(currQ.pop())


    return res


res = 0

def maxSum(root):
    global res
    if root == None:
        return 0

    l = maxSum(root.left)
    r = maxSum(root.right)


    res = max(res, l + r + root.val)

    return root.val + max(l, r)

if __name__ == '__main__':


    root = toTree()

    inorder(root)
    maxSum(root)

    print(res)

