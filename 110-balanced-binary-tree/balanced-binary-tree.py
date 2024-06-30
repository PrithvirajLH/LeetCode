# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def count(root):
            if not root:
                return 0
            left = count(root.left)
            right = count(root.right)
            if left<0 or right<0 or abs(left - right) > 1: 
                return -1
            return 1 + max(left,right)
        return count(root) >= 0
            
        