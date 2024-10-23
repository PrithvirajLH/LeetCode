class Solution:
    def trimMean(self, arr: List[int]) -> float:
        if len(arr) == 0:
            return 0
        n = len(arr)
        x = (n * 5) // 100

        arr.sort()

        return sum(arr[x: n-x]) / (n - (2*x))



        