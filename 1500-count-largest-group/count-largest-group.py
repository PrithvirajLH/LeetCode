class Solution:
    def countLargestGroup(self, n: int) -> int:
        for_ans = defaultdict(int)

        for i in range(1, n+1):
            total = 0
            num = i
            while num > 0:
                total += num%10
                num //= 10
            for_ans[total] += 1
        
        max_group = max(for_ans.values())
        ans = sum(1 for size in for_ans.values() if size == max_group)
        return ans

