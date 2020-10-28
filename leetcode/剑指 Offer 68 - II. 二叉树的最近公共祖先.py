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
    traver(root.left)
    traver(root.right)


'''
3 9 20 None None 15 7
4 2 7 1 3 6 9
3 5 1 6 2 0 8 null null 7 4
'''


def findNode(root, val):
    if root == None:
        return None

    if root.val == val:
        return root


    left = findNode(root.left, val)
    right = findNode(root.right, val)

    if left != None:
        return left
    return right


def lowestCommonAncestor(root, p, q):
    if root == None or root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left == None or right == None:
        return right if left == None else left

    return root


if __name__ == '__main__':
    root = toTree()
    traver(root)
    p = findNode(root, '5')
    q = findNode(root, '1')


    ancestor = lowestCommonAncestor(root, p, q)

    print(ancestor.val)
