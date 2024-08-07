class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter(s1)
        n = len(s1)
        for i in range(len(s2)):
            if s2[i] in s1_map:
                s1_map[s2[i]] -= 1
            if i >= n and s2[i-n] in s1_map:
                s1_map[s2[i-n]] += 1

            if all([s1_map[i] == 0 for i in s1_map]):
                return True

        return False 
            


        



        