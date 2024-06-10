class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        visit = []
        ans = []
        def dfs(x,y):
            if (x,y) in visit:
                return
            if (0 <= x < len(matrix) and 0 <= y < len(matrix[0])) is False:
                return

            visit.append((x,y))
            ans.append(matrix[x][y])

            if x -1 <= y:
                dfs(x,y+1)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x-1,y)
            
        dfs(0,0)
        
        return ans

