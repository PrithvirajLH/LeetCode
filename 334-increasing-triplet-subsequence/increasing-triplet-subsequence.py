class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        prefix = [0] * len(nums) 
        mini = nums[0]

        for i in range(len(nums)):
            prefix[i] = mini
            mini = min(mini, nums[i])

        postfix = [0] * len(nums)
        maxi = nums[-1]

        for i in range(len(nums)-1,-1,-1):
            postfix[i] = maxi
            maxi = max(maxi, nums[i])
        
        for i in range(len(nums)):
            if prefix[i] < nums[i] and nums[i] < postfix[i] :
                return True
        
        return False