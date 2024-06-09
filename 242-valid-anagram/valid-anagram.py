class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def mapping(word):
            maps = {}
            for char in word:
                if char in maps:
                    maps[char] += 1
                else:
                    maps[char] = 1
            return maps
        
        str1 = mapping(s)
        str2 = mapping(t)

        if str1 == str2:
            return True
        else:
            return False
        