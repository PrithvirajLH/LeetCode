# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # ans = []
        # def inorder(node):
        #     if not node:
        #         ans.append(-1)
        #         return
        #     inorder(node.left)
        #     ans.append(node.val)
        #     inorder(node.right)
        # inorder(root)
        # print(ans)
        # if ans == ans[::-1]:
        #     return True
        # else:
        #     return False        

        def isSame(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return isSame(root1.left, root2.right) and isSame(root1.right, root2.left)
        return isSame(root.left, root.right)