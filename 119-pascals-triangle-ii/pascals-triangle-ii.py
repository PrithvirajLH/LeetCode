class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # ans = [[1]]
        # for i in range(rowIndex):
        #     prev = ans[-1]
        #     curr = []
        #     curr.append(1)
        #     for j in range(len(prev)-1):
        #         curr.append(prev[j]+prev[j+1])
        #     curr.append(1)
        #     ans.append(curr)
        # return ans[-1]
        ans = [1]
        for i in range(1, rowIndex+1):
            ans.append(ans[-1] * (rowIndex - i + 1) // i)
        return ans
        
