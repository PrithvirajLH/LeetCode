class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict1 = Counter(arr)
        curr = []
        for i in dict1.values():
            if i in curr:
                return False
            else:
                curr.append(i)
        return True
        