class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        zeros = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.append((i,j))
        while zeros:
            (row,col) = zeros.pop()

            for i in range(n):
                matrix[row][i] = 0
            
            for j in range(m):
                matrix[j][col] = 0
            
            for k in range(n-1,-1,-1):
                matrix[row][k] = 0
            
            for l in range(m-1, -1,-1):
                matrix[l][col] = 0