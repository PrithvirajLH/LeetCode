# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        def dfs(root, path):
            if root:
                path += str(root.val)

                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += '->'
                    dfs(root.left, path)
                    dfs(root.right, path)
        dfs(root, "")
        return paths
            

