class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                index, temp = stack.pop()
                ans[index] = i - index
            stack.append((i, t))
        return ans







        # ans = []
        # for i in range(len(temperatures)):
        #     for j in range(i,len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             ans.append(j-i)
        #             break
        #         else:
        #             continue
        #     if len(ans)-1 != i:
        #         ans.append(0)
        # return ans

