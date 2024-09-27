class Solution:
    def smallestNumber(self, num: int) -> int:
        zero = 0
        minheap = []
        n = num
        if n > 0:
            while n > 0:
                temp = n % 10
                if temp == 0:
                    zero += 1
                else:
                    minheap.append(temp)
                n = n // 10
        else:
            n = n * (-1)
            while n > 0:
                temp = n % 10
                minheap.append(-temp)
                n = n // 10
        
        heapq.heapify(minheap)
        if num > 0:
            res = heapq.heappop(minheap)
            for _ in range(zero):
                heapq.heappush(minheap, 0)
        else:
            res = 0
        
        for _ in range(len(minheap)):
            res = res * 10
            res += heapq.heappop(minheap)
        
        return res
        



