class Solution:
    def isHappy(self, n: int) -> bool:
        a = n
        ans = []
        while True:
            sum = 0
            while a != 0:
                temp = a % 10
                sum += pow(temp,2)
                a = a // 10
            if sum == 1:
                return True
            if sum in ans:
                return False
            ans.append(sum)
            a = sum
        