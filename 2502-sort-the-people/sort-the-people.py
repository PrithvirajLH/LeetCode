class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dict1 = {}
        res = []
        for i in range(len(names)):
            dict1[heights[i]] = names[i]
        
        heights.sort(reverse=True)

        for j in range(len(names)):
            res.append(dict1[heights[j]])
        return res
