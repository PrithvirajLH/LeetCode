class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = []
        res = []


        def backtrack(i, j, idx):
            if i<0 or j<0 or i==rows or j==cols or idx == len(word) or (i,j) in visited or board[i][j] != word[idx]:
                return
            if idx < len(word):
                visited.append((i,j))
                res.append(word[idx])
                backtrack(i-1,j,idx+1)
                backtrack(i+1, j, idx+1)
                backtrack(i, j-1, idx+1)
                backtrack(i, j+1, idx+1)
            if len(res) != len(word):
                res.pop()
                visited.pop()


        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    backtrack(i, j, 0)

                    if ''.join(res) == word:
                        return True
                    else:
                        res = []
                        visited=[]
        
        return False

        