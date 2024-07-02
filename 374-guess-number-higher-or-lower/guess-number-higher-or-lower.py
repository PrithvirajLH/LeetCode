# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        first = 1
        last = n
        while first <= last:
            mid = (first + last) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == 1:
                first = mid + 1
            else:
                last = mid - 1

        