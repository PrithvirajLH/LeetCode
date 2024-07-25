class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        dict1 = Counter(nums1)
        dict2 = Counter(nums2)
        answer = []
        curr = []
        for i in dict1.keys():
            if i not in dict2:
                curr.append(i)
        answer.append(curr)
        curr = []
        for j in dict2.keys():
            if j not in dict1:
                curr.append(j)
        answer.append(curr)

        return answer
    


        