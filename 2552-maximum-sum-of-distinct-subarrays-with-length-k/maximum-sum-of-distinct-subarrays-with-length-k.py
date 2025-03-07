class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prev = {}
        currSum = 0
        l = 0

        for r in range(len(nums)):
            currSum += nums[r]
            i = prev.get(nums[r], -1)

            while l <= i or r-l+1 > k:
                currSum -= nums[l]
                l += 1

            if r-l+1 == k:
                res = max(res, currSum)
            
            prev[nums[r]] = r
        return res


