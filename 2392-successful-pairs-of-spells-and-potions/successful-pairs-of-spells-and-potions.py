class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:       
        ans = [] 
        potions.sort()
        for i in spells:
            left = 0
            right = len(potions) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if potions[mid] * i >= success:
                    # temp += right - mid + 1
                    right = mid - 1
                else:
                    left = mid + 1
            ans.append(len(potions) - right - 1)
        return ans

        # ans = []
        # for i in spells:
        #     count = 0
        #     for j in potions:
        #         if i * j >= success:
        #             count += 1
        #     ans.append(count)            
        # return ans