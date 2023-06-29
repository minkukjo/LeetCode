from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        def bfs(i,j):
            visit.add((i,j))
            q = deque()
            q.append((i,j))

            result = 1

            while q:
                (i,j) = q.pop()

                dx = [0,0,1,-1]
                dy = [1,-1,0,0]

                for k in range(4):
                    if i + dx[k] >= 0 and i + dx[k] < len(grid) and j + dy[k] >= 0 and j+ dy[k] < len(grid[0]) and grid[i + dx[k]][j + dy[k]] == 1 and (i+dx[k],j+dy[k]) not in visit:
                        visit.add((i+dx[k], j+dy[k]))
                        q.append((i+dx[k], j+dy[k]))
                        result += 1
            return result

        r = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visit and grid[i][j] == 1:
                    temp = bfs(i,j)
                    r = max(r, temp)
        return r