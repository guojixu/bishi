
from queue import Queue
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def buildTree():

    s = input().split()

    root = TreeNode(s[0])

    myque = deque()
    myque.appendleft(root)

    curr_index = 1

    while curr_index < len(s):

        node = myque.pop()
        currNum = s[curr_index]

        curr_index += 1
        if currNum != 'null':
            node.left = TreeNode(currNum)
            myque.appendleft(node.left)
        if curr_index > len(s):
            break
        currNum = s[curr_index]
        curr_index += 1

        if currNum != 'null':
            node.right = TreeNode(currNum)
            myque.appendleft(node)

    return root




def mirrorTree(root):

    if root == None:
        return

    left = root.left
    right = root.right

    root.left = mirrorTree(right)
    root.right = mirrorTree(left)

def mergeTree(t1, t2):

    if t1 == None and t2 == None:
        return None

    if t1 == None or t2 == None:

        return t2 if t1 == None else t1
    t1.val = t1.val + t2.val
    t1.left = mergeTree(t1.left, t2.left)
    t1.right = mergeTree(t1.right, t2.right)

    return t1

def invertTree(root):

    if root == None:
        return None

    right = invertTree(root.right)
    left = invertTree(root.left)

    root.left = right
    root.right = left

    return root

def showTree(root):
    if root == None:
        return

    showTree(root.left)
    print(root.val)
    showTree(root.right)



if __name__ == '__main__':


    root1 = buildTree()

    showTree(root1)


    # mirrorTree(root)

