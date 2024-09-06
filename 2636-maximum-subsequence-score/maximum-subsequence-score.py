class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        merged = [(nums2[i], nums1[i]) for i in range(len(nums1))]
        merged.sort(reverse = True)

        res = 0
        totalSum = 0
        heap = []

        for max2, num1 in merged:
            if len(heap) == k:
                totalSum -= heapq.heappop(heap)

            totalSum += num1
            heapq.heappush(heap, num1)

            if len(heap) == k:
                res = max(res, totalSum * max2)
        return res

        



