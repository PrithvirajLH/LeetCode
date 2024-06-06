class Solution(object):
    def isPalindrome(self, x):
        a = x
        z = 0
        while x > 0:
            y = x % 10
            z = z*10 + y
            x = x/10

        if a==z:
            return True
        else:
            return False
        