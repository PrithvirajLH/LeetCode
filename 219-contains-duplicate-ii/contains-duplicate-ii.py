class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        maps = {}

        for i, n in enumerate(nums):
            if n in maps and i - maps[n] <= k:
                return True
            maps[n] = i
        return False
