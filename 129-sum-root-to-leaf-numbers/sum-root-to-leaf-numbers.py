# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(res, root):
            if not root:
                return 0
            res = res * 10 + root.val
            if not root.left and not root.right:
                return res
            return dfs(res,root.left) + dfs(res,root.right) 
        return dfs(0, root)

        