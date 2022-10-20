
class Solution(object):
    def preorder(self, root):
        def touch(root, ans):
            if root:                         
                ans.append(root.val)         
                for child in root.children:   
                    touch(child, ans)
            return ans
        return touch(root, [])