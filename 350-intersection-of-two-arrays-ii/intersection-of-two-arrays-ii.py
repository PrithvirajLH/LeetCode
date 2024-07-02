class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # ans = []
        # def helper(arr1, arr2):
        #     for i in arr1:
        #         if i in arr2:
        #             ans.append(i)
        #             arr2.remove(i)
        # if len(nums1) <= len(nums2):
        #     helper(nums1,nums2)
        # else:
        #     helper(nums2,nums1)
        # return ans
        
        hashMap = Counter(nums1)
        ans = []

        for num in nums2:
            if hashMap[num] > 0:
                hashMap[num] -= 1
                ans.append(num)
        return ans