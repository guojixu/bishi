
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def toTree():

    s = input().split()

    root = TreeNode(s[0])
    nodeQueue = [root]

    front = 0
    index = 1

    while index < len(s):

        node = nodeQueue[front]

        front = front + 1

        item = s[index]

        index = index + 1

        if item != 'null':
            leftVal = item
            node.left = TreeNode(leftVal)
            nodeQueue.append(node.left)

        if index >= len(s):
            break

        item = s[index]
        index = index + 1

        if item != 'null':
            rightVal = item

            node.right = TreeNode(rightVal)

            nodeQueue.append(node.right)

    return root



def traver(root):

    if root == None:
        return
    print(root.val)

    traver(root.left)
    traver(root.right)


def depth(root):

    if root == None:
        return 0
    lh = depth(root.left)
    rh = depth(root.right)

    return max(lh, rh) + 1

def levelOrder(root):

    myque = deque()

    myque.appendleft(root)

    while len(myque) > 0:

        curr_queue = deque()

        while len(myque) > 0:

            currNode = myque.pop()

            print(currNode.val, end=' ')
            if currNode.left != None:
                curr_queue.appendleft(currNode.left)
            if currNode.right != None:
                curr_queue.appendleft(currNode.right)


        while len(curr_queue) > 0:
            myque.appendleft(curr_queue.pop())

        print("")




'''
3 9 20 null null 15 7
4,2,7,1,3,6,9
'''


if __name__ == '__main__':
    root = toTree()
    traver(root)
    levelOrder(root)