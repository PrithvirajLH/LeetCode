class Solution:
    def reverse(self, x: int) -> int:
        flag = 0
        if x < 0 :
            x = x * -1
            flag = 1
        n = x
        ans = 0
        while n!=0:
            temp = n % 10
            ans = ans * 10 + temp
            n = n // 10
        
        
        if flag:
            ans *= -1
        if ans > pow(-2,31) and ans < pow(2,31):
            return(ans)
        else:
            return(0)
            