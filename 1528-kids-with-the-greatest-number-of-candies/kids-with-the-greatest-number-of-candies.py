class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        ans = [True] * len(candies)
        for i in range(len(candies)):
            currSum = candies[i] + extraCandies
            if currSum < greatest:
                ans[i] = False
        return ans

        