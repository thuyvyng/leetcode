class Solution(object):
    def searchBST(self, root, val):
        def rec(root):
            if root:
                if root.val == val: return root
                elif root.val < val: return rec(root.right)
                return rec(root.left)
            return None
        return rec(root)