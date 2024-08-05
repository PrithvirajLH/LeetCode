class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSize = float('inf')
        currSum = 0
        start = 0
        for i in range(len(nums)):
            currSum += nums[i]
            while currSum >= target and start < len(nums):
                minSize = min(minSize, i - start + 1)
                currSum -= nums[start]
                start += 1
        return 0 if minSize == float('inf') else minSize





        