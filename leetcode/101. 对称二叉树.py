
class Solution:
    def isSymmetric(self, root) -> bool:

        def helper(l, r):
            if l == None and r == None:
                return True
            elif l == None and r != None:
                return False
            elif l != None and r == None:
                return False

            return l.val == r.val and helper(l.left, r.right) and helper(l.right, r.left)

        return helper(root, root)


