from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binSearch(l,r,nums):
            if l<=r:
                mid = (l+r) // 2

                if nums[mid] == target:
                    return mid

                if nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            
                return binSearch(l,r,nums)
            return -1


        for i in range(len(matrix)):
            if matrix[i][len(matrix[i])-1] < target:
                continue

            if(binSearch(0,len(matrix[i])-1,matrix[i]) == -1):
                return False
            else:
                return True
                

