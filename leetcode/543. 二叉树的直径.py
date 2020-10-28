

res = 0

def maxDia(root):

    global res
    if root == None:
        return 0

    lh = maxDia(root.left)
    rh = maxDia(root.right)

    res = max(res, lh + rh + 1)

    return max(lh, rh) + 1

