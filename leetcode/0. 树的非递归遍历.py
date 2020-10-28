
def preorder(root): # 先序
        stack = []
        while stack or root:
            while root:
                print(root.val)
                stack.append(root)
                root = root.lchild
            root = stack.pop()
            root = root.rchild

def inorder(root): # 中序
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.lchild
            root = stack.pop()
            print(root.val)
            root = root.rchild

def inorder(root):
    stack = []

    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        root = root.rchild

def postorder(root):

    res = deque()

    stack = deque()

    p = root

    while p != None or len(stack) > 0:
        while p != None:

            res.appendleft(p.val)
            stack.append(p)
            p = p.right
        p = stack.pop()

        p = p.left

def postorder(root): # 后序
    stack = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.lchlid if root.lchild else root.right
        root = stack.pop()
        print(root.val)
        if stack and stack[-1].lchild == root:
            root = stack[-1].rchild
        else:
            root = None


from collections import deque
def postorderTraversal(self, root):

    res = deque()

    stack = deque()

    p = root

    while p != None or len(stack) > 0:

        while p != None:
            res.appendleft(p.val)
            stack.append(p)
            p = p.right
        p = stack.pop()
        p = p.left

    return res



