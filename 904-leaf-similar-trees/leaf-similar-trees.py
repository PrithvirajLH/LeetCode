# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaf(root):
            ans = []
            stack = [root]

            while stack:
                node = stack.pop()
                if node:
                    if not node.left and not node.right:
                        ans.append(node.val)
                    stack.append(node.right)
                    stack.append(node.left)
                    
            return ans
        a = getLeaf(root1)
        b = getLeaf(root2)
        print(a)
        print(b)
        return a == b