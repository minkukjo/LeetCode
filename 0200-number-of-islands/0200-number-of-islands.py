class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        def dfs(grid, x, y):
            if grid[x][y] != "1":
                return
            
            grid[x][y] = "#"

            if x + 1 < len(grid) and grid[x+1][y] == "1":
                dfs(grid, x+1, y)
            if 0 <= x -1 and grid[x-1][y] == "1":
                dfs(grid, x-1, y)
            if y + 1 < len(grid[0]) and grid[x][y+1] == "1":
                dfs(grid, x,y+1)
            if 0 <= y-1 and grid[x][y-1] == "1":
                dfs(grid, x,y-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(grid, i,j)
                    result += 1

        return result