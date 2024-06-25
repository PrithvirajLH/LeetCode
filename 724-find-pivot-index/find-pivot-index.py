class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # res = [0] * len(nums)
        # prefix = 0
        # for i in range(len(nums)):
        #     res[i] = prefix
        #     prefix += nums[i]
        # postfix = 0
        # for i in range(len(nums)-1, -1, -1):
        #     res[i] -= postfix
        #     if res[i] == 0:
        #         return i
        #     postfix += nums[i]
        # return -1

        res = [0] * len(nums)
        postfix = 0
        for i in range(len(nums)-1,-1,-1):
            res[i] = postfix
            postfix += nums[i]
        prefix = 0
        for i in range(len(nums)):
            res[i] -= prefix
            if res[i] == 0:
                return i
            prefix += nums[i]
        return -1
         
        