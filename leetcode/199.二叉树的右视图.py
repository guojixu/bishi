

from collections import deque

class TreeNode:
    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None


def toTree():

    s = input().split(',')

    root = TreeNode(s[0])

    myQ = deque()

    myQ.appendleft(root)

    curr_index = 1

    while curr_index < len(s):

        currNode = myQ.pop()

        currVal = s[curr_index]
        curr_index += 1

        if currVal != 'null':
            currNode.left = TreeNode(currVal)
            myQ.appendleft(currNode.left)

        if curr_index > len(s):
            break

        currVal = s[curr_index]
        curr_index += 1

        if currVal != 'null':
            currNode.right = TreeNode(currVal)
            myQ.appendleft(currNode.right)



    return root
#
# def toTree():
#     s = input().split()
#
#     myqueue = deque()
#
#     root = TreeNode(s[0])
#     myqueue.appendleft(root)
#
#     curr_index = 1
#
#     while curr_index < len(s):
#
#         node = myqueue.pop()
#
#         curr_val = s[curr_index]
#         curr_index += 1
#
#
#         if curr_val != 'null':
#             node.left = TreeNode(curr_val)
#             myqueue.appendleft(node.left)
#
#         if curr_index >= len(s):
#             break
#
#         curr_val = s[curr_index]
#         curr_index += 1
#
#         if curr_val != 'null':
#             node.right = TreeNode(curr_val)
#             myqueue.appendleft(node.right)
#
#     return root

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

            currList.append(currNode.val)

            if currNode.left != None:
                currQ.appendleft(currNode.left)

            if currNode.right != None:
                currQ.appendleft(currNode.right)

        res.append(currList)

        while len(currQ) > 0:
            myQ.appendleft(currQ.pop())


    return res



def dfs(root, depth):

    global ans
    if root == None:
        return

    if depth == len(ans):
        ans.append(root.val)
    depth += 1
    dfs(root.right, depth)
    dfs(root.left, depth)

def rightSideView(root):

    dfs(root, 0)


if __name__ == '__main__':
    ans = []

    root = toTree()

    # inorder(root)
    #
    # print(levelOrder(root))


    rightSideView(root)

    print(ans, 'rightview')