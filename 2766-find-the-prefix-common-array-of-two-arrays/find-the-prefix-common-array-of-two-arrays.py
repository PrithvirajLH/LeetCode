class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        common = 0
        res = [0] * n
        count_a = [0] * (n+1)
        count_b = [0] * (n+1)

        for i in range(n):
            j = A[i]
            k = B[i]
            count_a[j] += 1
            count_b[k] += 1

            if count_a[j]==1 and count_b[j] == 1:
                common += 1
            if j!= k and count_a[k] == 1 and count_b[k] == 1:
                common += 1
            
            res[i] = common
        
        return res

        
        