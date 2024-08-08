class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map1 = {}
        map2 = {}

        words = s.split()

        if len(words) != len(pattern):
            return False
        
        for p, w in zip(pattern, words):
            if p in map1 and map1[p] != w:
                return False
            if w in map2 and map2[w] != p:
                return False
            
            map1[p] = w
            map2[w] = p
        return True


        