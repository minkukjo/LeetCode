class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def dfs(x,y):
            
            s = set()

            for i in range(x, x+3):
                for j in range(y, y+3):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in s:
                        return False
                    s.add(board[i][j])
            return True
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                if dfs(i,j) is False:
                    return False
        
        # 가로열 중복 체크
        for i in range(0,9):
            s = set()
            for j in range(0,9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])
        
        # 세로열 중복 체크
        for i in range(0,9):
            s = set()
            for j in range(0,9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in s:
                    return False
                s.add(board[j][i])
        
        return True

