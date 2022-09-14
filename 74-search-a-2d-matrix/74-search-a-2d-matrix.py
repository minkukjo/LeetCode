class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(matrix: List[int], col, target):
            left = 0
            right = col

            while left <= right:
                mid = (left+right) // 2

                if matrix[mid] < target:
                    left = mid +1
                elif matrix[mid] > target:
                    right = mid -1
                else:
                    return matrix[mid]
            return -1

        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            if matrix[i][col-1] < target:
                continue
            else:
                result = binarySearch(matrix[i], col, target)
                if result == -1:
                    return False
                return True