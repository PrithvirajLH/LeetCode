class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in prices:
            temp = 0
            if i < buy:
                buy = i
            if i - buy > temp:
                profit += i - buy
                buy = i
        return profit
        