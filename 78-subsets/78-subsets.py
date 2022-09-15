class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
            
        def comb(arr, n):
            result = []
            
            if n == 0:
                return [[]]
        
            for i in range(len(arr)):
                elem = arr[i]
                for j in comb(arr[i+1:], n-1):
                    result.append([elem] + j)
            return result
        
        result = [[]]
        for i in range(1, len(nums)+1):
            result += comb(nums, i)
        return result