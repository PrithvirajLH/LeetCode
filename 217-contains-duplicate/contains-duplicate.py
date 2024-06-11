class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mydict  = {}
        for x in nums:
            if x in mydict:
                return True
            else:
                mydict[x] = 1
        return False
        