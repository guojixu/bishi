





from collections import deque


class HTreeNode:
    def __init__(self, node):

        self.id = int(node[0])
        self.val = int(node[1])

        if int(node[2]) == -1:
            self.left = None
        else:
            self.left = 'wait'
        if int(node[3]) == -1:
            self.right = None
        else:
            self.right = 'wait'



def toHTree():

    n = int(input())

    nodes = []

    for _ in range(n):
        nodes.append(input().split())

    root = HTreeNode(nodes[0])


    myQ = deque()

    myQ.appendleft(root)

    curr_index = 1

    while curr_index < len(nodes):



        currNode = myQ.pop()


        if currNode.left == None and currNode.right == None:

            continue

        if currNode.left != None:

            currVal = nodes[curr_index]

            curr_index += 1

            currNode.left = HTreeNode(currVal)
            myQ.appendleft(currNode.left)


        if curr_index > len(nodes):
            break

        if currNode.right != None:

            currVal = nodes[curr_index]
            curr_index += 1

            currNode.right = HTreeNode(currVal)

            myQ.appendleft(currNode.right)

    return root




def inorder(root):

    if root == None:
        return

    inorder(root.left)

    print(root.id)

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

            currList.append(currNode.id)

            if currNode.left != None:
                currQ.appendleft(currNode.left)

            if currNode.right != None:
                currQ.appendleft(currNode.right)

        res.append(currList)

        while len(currQ) > 0:
            myQ.appendleft(currQ.pop())


    return res




def helper(root, prev):

    global res

    if root == None:
        return

    res = max(res, prev ^ root.val)

    helper(root.left, prev ^ root.val)

    helper(root.right, prev ^ root.val)


def findmax(root):

    global res
    if root == None:
        return

    findmax(root.left)

    helper(root, 0)

    findmax(root.right)


if __name__ == '__main__':
    # root = toTree()

    root = toHTree()

    res = float('-inf')

    print(levelOrder(root))

    findmax(root)

    print(res)

    # print(levelOrder(root))

'''
5
1 1 2 3
2 4 -1 -1
3 2 -1 4
4 5 -1 5
5 3 -1 -1

7
'''

