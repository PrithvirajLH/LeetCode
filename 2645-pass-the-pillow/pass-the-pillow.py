class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        flag = 1
        i = 1
        while time != 0:
            if flag:
                i += 1
                time -= 1
                if i == n:
                    flag = 0
            else:
                i -= 1
                time -= 1
                if i == 1:
                    flag = 1
        return i

        