class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        result = [[1],[1,1]]
        for i in range(2, numRows):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(result[i-1][j-1] + result[i-1][j])
            result.append(temp)
        return result
