class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        for x in nums:
            if x in mydict:
                mydict[x] += 1
            else:
                mydict[x] = 1
        ans = []
        for key,v in mydict.items():
            heappush(ans,(v,key))
            if len(ans) > k:
                heappop(ans)
        top_numbers=[]
        while ans:
            top_numbers.append(heappop(ans)[1])
        return top_numbers