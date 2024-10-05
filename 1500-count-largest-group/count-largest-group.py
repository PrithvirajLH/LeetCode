class Solution:
    def countLargestGroup(self, n: int) -> int:
        mapping = {}
        for num in range(1, n+1):
            sums = 0
            while num != 0:
                sums += num % 10
                num //= 10
            mapping[sums] = mapping.get(sums,0) + 1
        
        max_val = max(mapping.values())
        count = 0
        for k, v in mapping.items():
            if v == max_val:
                count += 1
        return count
