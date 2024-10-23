class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxCount = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1
            else:
                continue
            

            maxCount = max(maxCount, count)
        return maxCount
