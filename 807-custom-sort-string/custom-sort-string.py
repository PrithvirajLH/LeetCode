class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        res = []
        for c in order:
            if c in count:
                res.append(c * count[c])
                del count[c]
        
        for c, freq in count.items():
            res.append(c*freq)
        
        return "".join(res)
        