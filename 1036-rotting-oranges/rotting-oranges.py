class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        q = deque()
        fresh = 0

        def add(r,c):
            nonlocal fresh
            if r<0 or c<0 or r>= rows or c>= cols or (r,c) in visit or grid[r][c] == 0:
                return
            q.append([r,c])
            visit.add((r,c))
            fresh -= 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        time = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = 2
                add(r-1, c)
                add(r+1, c)
                add(r, c-1)
                add(r, c+1)
            time += 1
        
        return time-1 if fresh == 0 else -1


        