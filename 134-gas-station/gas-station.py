class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gasSum = sum(gas)
        costSum = sum(cost)
        if costSum > gasSum:
            return -1
        
        currentGas = 0
        start = 0

        for i in range(len(gas)):
            currentGas += gas[i] - cost[i]
            if currentGas < 0:
                currentGas = 0
                start = i + 1
        return start
          
        
        
        
        
        
        # 31/ 40 Test cases passed
        # i = 0
        # # while gas[i] < cost[i]:
        # #     if i < len(gas):
        # #         i += 1
        # #     else:
        # #         return -1
        # min = float('inf')
        # for k in range(len(gas)):
        #     temp = cost[k] - gas[k]
        #     if temp < min:
        #         min = temp
        #         i = k
        # tank = gas[i] - cost[i]
        # start = i
        # if i == len(gas) - 1:
        #     i = 0
        # else:
        #     i += 1
        # while start != i:
        #     tank += gas[i]
        #     if tank >= cost[i]:
        #         tank = tank - cost[i]
        #         if i == len(gas) - 1:
        #             i = 0
        #         else:
        #             i += 1
        #     else:
        #         return -1
        # return start
                


        