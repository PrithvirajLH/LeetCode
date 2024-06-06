class Solution(object):
    def twoSum(self, nums, target):
        index = []

        for i in range (0, len(nums)):
            temp = target - nums[i]
            if temp in nums:
                check = nums.index(temp)
                if i != check:
                    index.append(i)
                    index.append(check)
                    break
        return index

                
        