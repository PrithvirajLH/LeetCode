class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0] * (len(gain)+1)
        prefix = 0
        for i in range(len(gain)):
            res[i] = prefix
            prefix += gain[i]
        res[-1] = prefix
        return max(res) 
        