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

def depth(root):
    if root == None:
        return 0

    lh = depth(root.left)
    rh = depth(root.right)

    return max(lh, rh) + 1

def showTree(root):
    if root == None:
        return

    showTree(root.left)
    print(root.val)
    showTree(root.right)

'''
3 9 20 null null 15 7
'''

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
    showTree(root)
    print(depth(root))

    rightSideView(root)
    print(ans)

