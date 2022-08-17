class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) -1

        for k in range(0, len(matrix)//2):
            for i in range(0+k, n-k):
                first = matrix[k][i]
                second = matrix[i][n-k]
                third = matrix[n-k][n-i]
                fourth = matrix[n-i][k]
                matrix[k][i] = fourth
                matrix[i][n-k] = first
                matrix[n-k][n-i] = second
                matrix[n-i][k] = third