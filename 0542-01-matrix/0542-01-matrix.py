class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        q = deque()
        d = [(0,1), (0,-1), (1,0), (-1,0)]

        for i in range(len(mat)):
            for j in range(len(mat[0])):

                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = float('inf')
        
        while q:
            x, y = q.popleft()

            for dx, dy in d:
                nx, ny = x+dx, y+dy

                if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]) and mat[nx][ny] > mat[x][y] + 1:
                    mat[nx][ny] = mat[x][y] + 1
                    q.append((nx,ny))
        return mat
                    






        
