class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [i for i in range(1,n+1)]
        index = 0
        while len(nums) != 1:
            remove = (index + k - 1) % len(nums)
            nums.pop(remove)
            index = remove
        return nums[0]
            




        