class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res = []
        arr.sort()
        diff = float('inf')
        for i in range(1, len(arr)):
            currDiff = arr[i] - arr[i-1]
            diff = min(currDiff, diff)
        
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] == diff:
                res.append([arr[i-1], arr[i]])
        return res