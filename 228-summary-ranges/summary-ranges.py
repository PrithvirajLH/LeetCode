class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        start = nums[0]
        ans =[]
        flag = False
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                flag = True
            else:
                if flag:
                    res = str(start) + "->" +str(nums[i-1])
                else:
                    res = str(start)
                ans.append(res)
                start = nums[i]
                flag = False
        if start == nums[len(nums)-1]:
            ans.append(str(start))
        else:
            ans.append(str(start) + "->" + str(nums[len(nums)-1]))
        
        return ans
            
            
