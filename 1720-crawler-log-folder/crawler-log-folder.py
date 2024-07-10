class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for i, a in enumerate(logs):
            if (count == 0 and a == "../") or a == "./":
                continue
            elif a == "../":
                count -= 1
            else:
                count += 1
        return count
        