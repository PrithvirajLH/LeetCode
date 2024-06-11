class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            if all(item == 9 for item in digits):
                ans = [0] * (len(digits)+1)
                ans[0] = 1
                return ans
            else:
                i = -1
                while digits[i]==9:
                    digits[i] = 0
                    i -= 1
                digits[i] +=1
        return digits
        

        