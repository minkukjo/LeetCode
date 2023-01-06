class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        result = 0
        visit = set()
        
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j,0))
        
        while q:
            row,col,time = q.popleft()
            visit.add((row,col))
            result = max(result, time)
            

            for i in range(4):
                nx = row + dx[i]
                ny = col + dy[i]
                if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
                    continue
                
                if grid[nx][ny] == 0 or grid[nx][ny] == 2 or (nx,ny) in visit:
                    continue
                
                if grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    q.append((nx,ny,time+1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return result
