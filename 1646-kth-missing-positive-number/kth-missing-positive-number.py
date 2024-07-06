class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # ans = 0
        # while k != 0:
        #     ans += 1
        #     if ans not in arr:
        #         k -= 1
        # return ans
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right ) // 2
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k
            
            
        