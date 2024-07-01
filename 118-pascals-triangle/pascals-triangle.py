class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(numRows-1):
            prev = ans[-1]
            curr = []
            curr.append(1)
            for j in range(len(prev)-1):
                curr.append(prev[j]+prev[j+1])
            curr.append(1)
            ans.append(curr)
        return ans
            