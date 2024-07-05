class Solution:
    def hammingWeight(self, n: int) -> int:
        num = int(format(n, 'b'))
        count = 0
        while num != 0:
            temp = num % 10
            if temp == 1:
                count += 1
            num = num // 10
        return count
        