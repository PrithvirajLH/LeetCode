class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        ans = []
        while val in nums:
            nums.remove(val)
        return len(nums)
            
        