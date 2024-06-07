class Solution(object):
    def romanToInt(self, s):
        maps = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        value = 0
        for i in range(len(s)):
            if i < len(s)-1 and maps[s[i]] < maps[s[i+1]]:
                value -= maps[s[i]]
            else:
                value +=maps[s[i]]
        return value