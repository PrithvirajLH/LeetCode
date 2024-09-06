class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            dist = math.sqrt((x**2)+(y**2))
            minHeap.append((dist, x, y))
        heapq.heapify(minHeap)
        res = []
        for _ in range(k):
            temp = heapq.heappop(minHeap)
            res.append(temp[1:])
        return res

        