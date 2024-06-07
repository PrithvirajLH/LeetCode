class Solution(object):
    def romanToInt(self, s):
        maps = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        y = s.replace('IV','IIII').replace('IX','VIIII').replace('XL', 'XXXX').replace('XC','LXXXX').replace('CD','CCCC').replace('CM','DCCCC')
        value=0

        for x in y:
            value += maps[x]
        return value