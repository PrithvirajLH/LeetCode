class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        def surround( r,c ):
            if r<0 or c<0 or r==rows or c==cols or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            surround(r-1, c)
            surround(r+1, c)
            surround(r, c-1)
            surround(r, c+1)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows-1] or c in [0, cols-1]):
                    surround(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'