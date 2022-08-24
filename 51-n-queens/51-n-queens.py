class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()
        board = [["."] * n for i in range(n)]
        result = []

        def backtracking(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return

            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                posDiag.add(r+c)
                negDiag.add(r-c)
                col.add(c)
                board[r][c] = "Q"

                backtracking(r+1)

                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        backtracking(0)
        return result