class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def toBST():

    nums = [int(_) for _ in input().split()]

    left = 0
    right = len(nums)

    def helper(nums, left, right):
        if left > right:
            return None

        mid = (left + right) // 2
        print(mid, 'mid')
        root = TreeNode(nums[mid])

        root.left = helper(nums, left, mid - 1)
        root.right = helper(nums, mid + 1, right)

        return root

    root = helper(nums, left, right-1)
    return root



def showtree(root):
    if root == None:
        return
    showtree(root.left)
    print(root.val)
    showtree(root.right)

# -10 -3 0 5 9

if __name__ == '__main__':

    root = toBST()
    showtree(root)






