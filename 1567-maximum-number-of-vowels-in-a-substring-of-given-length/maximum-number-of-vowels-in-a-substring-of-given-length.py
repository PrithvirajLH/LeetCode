class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        currCount = 0
        vowels = 'aeiou'

        for char in s[:k]:
            if char in vowels:
                currCount += 1
        
        maxCount = currCount

        i = 0
        while i < (len(s) - k):
            currCount = currCount - (s[i] in vowels) + (s[i+k] in vowels)
            maxCount = max(maxCount, currCount)
            i += 1

        return maxCount 


        
        