class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        sums = 1
        for i in range (n//2):
            sums = sums * 2
            if sums == n:
                return True
            elif sums > n:
                return False

