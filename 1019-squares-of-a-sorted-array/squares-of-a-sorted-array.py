class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        ans = deque()
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])

            if left > right:
                ans.appendleft(left*left)
                l += 1
            else:
                ans.appendleft(right * right)
                r -= 1
        return list(ans)

        