class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                fast = 0
                while True:
                    slow = nums[slow]
                    fast = nums[fast]
                    if slow == fast:
                        return slow
                
        
