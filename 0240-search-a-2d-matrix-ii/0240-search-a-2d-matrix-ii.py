class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        last = n - 1

        def binray_search(arr):
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = (left + right) // 2

                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    right = mid-1
                elif arr[mid] < target:
                    left = mid+1

            return False

        for i in range(m):
            if matrix[i][last] < target:
                continue
            
            if binray_search(matrix[i]):
                return True
        return False