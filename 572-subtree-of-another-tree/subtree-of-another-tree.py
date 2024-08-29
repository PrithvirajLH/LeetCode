# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            return isSame(a.left, b.left) and isSame(a.right, b.right)
        
        def check(root, subRoot):
            if not root:
                return False
            if not subRoot:
                return True
            
            if isSame(root, subRoot):
                return True
            
            return check(root.left, subRoot) or check(root.right, subRoot)
        return check(root, subRoot)
        