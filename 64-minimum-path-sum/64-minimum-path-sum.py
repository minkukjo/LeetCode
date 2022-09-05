class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        memo = {}
        def dfs(row, col):
            if (row, col) == (len(grid)-1, len(grid[0])-1):
                return grid[row][col]
            
            if row > len(grid)-1 or col > len(grid[0])-1:
                return float('inf')
            
            if (row,col) in memo:
                return memo[(row,col)]
            
            result = grid[row][col] + min(dfs(row+1,col), dfs(row,col+1))
            memo[(row,col)] = result
            return result
            
        return dfs(0,0)