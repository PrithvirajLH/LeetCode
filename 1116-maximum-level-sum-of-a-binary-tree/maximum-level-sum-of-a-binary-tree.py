# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        minLevel = 1
        queue = deque()
        queue.append(root)
        level = 1
        maxSum = float('-inf')
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if level_sum > maxSum:
                maxSum = level_sum
                minLevel = level
            
            level += 1
        return minLevel



        