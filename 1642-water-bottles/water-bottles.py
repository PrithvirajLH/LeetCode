class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = numBottles
        while numBottles >= numExchange:
            quo, rem = divmod(numBottles, numExchange)
            count += quo
            numBottles = quo + rem
        return count
        