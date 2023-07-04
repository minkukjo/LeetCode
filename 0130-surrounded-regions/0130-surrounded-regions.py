class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def dfs(r, c):
            if board[r][c] == 'O':
                board[r][c] = 'Z'
                for dr, dc in (-1, 0), (0, 1), (1, 0), (0, -1):
                    i, j= r + dr, c + dc
                    if 0<=i<len(board) and 0<j<len(board[0]):
                        dfs(i,j)

        for i in range(len(board)):
            dfs(i,0)
            dfs(i,len(board[0])-1)
        
        for j in range(len(board[0])):
            dfs(0,j)
            dfs(len(board)-1,j)

        for i  in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "Z":
                    board[i][j] = "O"
                else:
                    board[i][j] ='X'