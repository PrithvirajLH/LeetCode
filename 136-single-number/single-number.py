class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mydict = {}
        for i in nums:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1
        
        for k,v in mydict.items():
            if v == 1:
                return k
        