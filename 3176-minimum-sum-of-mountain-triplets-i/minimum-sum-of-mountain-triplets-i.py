class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        # ans = float(inf)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] < nums[j] and nums[k] < nums[j]:
        #                 currSum = nums[i] + nums[j] + nums[k]
        #                 ans = min(ans,currSum)
        # if ans == float(inf):
        #     return -1
        # else:
        #     return ans

        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        minPrefix = float('inf')
        for i in range(len(nums)):
            prefix[i] = minPrefix
            minPrefix = min(minPrefix, nums[i])
        minPostfix = float('inf')
        for i in range(len(nums)-1,-1,-1):
            postfix[i] = minPostfix
            minPostfix = min(minPostfix, nums[i])
        ans = float('inf')
        for i in range(1,len(nums)-1):
            if prefix[i] < nums[i] and postfix[i] < nums[i]:
                ans = min(ans, prefix[i]+nums[i]+postfix[i])
        if ans == float('inf'):
            return -1
        else:
            return ans
