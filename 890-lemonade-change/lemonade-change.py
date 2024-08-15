class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        denomination = { 5: 0, 10: 0, 20: 0}
        money = 0
        for i in bills:
            denomination[i] += 1
            if i == 10 and denomination[5] > 0:
                denomination[5] -= 1
            elif i == 20:
                if denomination[10] > 0 and denomination[5] > 0:
                    denomination[10] -= 1
                    denomination[5] -= 1
                elif denomination[5] > 2:
                    denomination[5] -= 3
                else:
                    return False
            elif i == 5:
                continue
            else:
                return False
        return True
             


        