class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1 = {}
        for i in range(len(magazine)):
            if magazine[i] in dict1:
                dict1[magazine[i]] += 1
            else:
                dict1[magazine[i]] = 1
        
        for i in range(len(ransomNote)):
            if ransomNote[i] in dict1 and dict1[ransomNote[i]]>0:
                dict1[ransomNote[i]] -= 1
            else:
                return False
        return True
            

        