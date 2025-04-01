class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        maxNum = "0"
        max_i = -1
        swap_i = -1
        swap_j = -1

        for i in range(len(nums)-1, -1, -1):
            if nums[i] > maxNum:
                maxNum = nums[i]
                max_i = i
            if nums[i] < maxNum:
                swap_i, swap_j = max_i, i
        nums[swap_i], nums[swap_j] = nums[swap_j], nums[swap_i]

        return int("".join(nums))