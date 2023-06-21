class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        result = 0

        def bfs(i,j):
            if (i,j) in visit or grid[i][j] == "0":
                return
            q = deque()
            q.append((i,j))
            visit.add((i,j))
            
            while q:
                (i,j) = q.popleft()

                if i+1 < len(grid) and grid[i+1][j] == "1":
                    q.append((i+1,j))
                    grid[i+1][j] = "0"
                    visit.add((i+1,j))

                
                if j+1 < len(grid[0]) and grid[i][j+1] == "1":
                    q.append((i,j+1))
                    grid[i][j+1] = "0"
                    visit.add((i,j+1))
                
                if i-1 >= 0 and grid[i-1][j] == "1":
                    q.append((i-1,j))
                    grid[i-1][j] = "0"
                    visit.add((i-1,j))

                
                if j-1 >= 0 and grid[i][j-1] == "1":
                    q.append((i,j-1))
                    grid[i][j-1] = "0"
                    visit.add((i,j-1))
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visit:
                    bfs(i,j)
                    result += 1
        return result



            

