class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c] == '0'):
                return
            grid[r][c] = '0'
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        
        rows, cols = len(grid), len(grid[0])
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res









        # if not grid:
        #     return 0
        # rows, cols = len(grid), len(grid[0])
        # visited = set()
        # islands = 0

        # def bfs(r, c):
        #     q = deque()
        #     visited.add((r, c))
        #     q.append((r,c))
        #     while q:
        #         row, col = q.popleft()
        #         directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        #         for dr, dc in directions:
        #             r = row + dr
        #             c = col + dc
        #             if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visited):
        #                 q.append((r,c))
        #                 visited.add((r,c))

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r,c) not in visited:
        #             bfs(r, c)
        #             islands += 1
        # return islands