class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        table = defaultdict(int)
        count = 0

        for row in grid:
            table[str(row)] += 1
        
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            count += table[str(col)]
        return count
        

        