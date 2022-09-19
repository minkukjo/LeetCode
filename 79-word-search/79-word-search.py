class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        path = set()
        s = ''
        for r in range(row):
            for c in range(col):
                s += board[r][c]
        for w in word:
            if w not in s:
                return False
        def dfs(r, c, i):
            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] != word[i] or (r, c) in path:
                return False
            if board[r][c] == word[i] and i == len(word) - 1:
                return True
            
            path.add((r, c))
            res = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) 
                   or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            path.remove((r, c))
            
            return res
        
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False