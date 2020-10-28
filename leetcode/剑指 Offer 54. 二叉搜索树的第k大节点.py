from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def toTree():
    s = input().split()

    myqueue = deque()

    root = TreeNode(s[0])
    myqueue.appendleft(root)

    curr_index = 1

    while curr_index < len(s):

        node = myqueue.pop()

        curr_val = s[curr_index]
        curr_index += 1

        if curr_val != 'null':
            node.left = TreeNode(curr_val)
            myqueue.appendleft(node.left)

        if curr_index >= len(s):
            break

        curr_val = s[curr_index]
        curr_index += 1

        if curr_val != 'null':
            node.right = TreeNode(curr_val)
            myqueue.appendleft(node.right)

    return root


def showTree(root):
    if root == None:
        return

    showTree(root.left)
    print(root.val)
    showTree(root.right)


res = 0
k = 3


def findKTree(root):

    def helper(root):
        global k, res

        if root == None:
            return

        helper(root.right)
        if k == 0:
            return
        k -= 1

        if k == 0:
            res = root.val

        helper(root.left)

    helper(root)
    return res


'''
3 9 20 null null 15 7
5 3 6 2 4 null null 1
3
'''

if __name__ == '__main__':
    root = toTree()
    showTree(root)
    print(findKTree(root))

